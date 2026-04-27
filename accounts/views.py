from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from accounts.forms import UpdateMemberForm, MessageForm
from .models import Members, Messages
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST': # Donkey clicked 'Submit'
        form = UserCreationForm(request.POST)
        if form.is_valid(): # Did the donkey fill it right?
            user = form.save() # Save the donkey to the database
            login(request, user) # Automatically log them in
            return redirect('home') # Send them to the homepage
    else: # Donkey just arrived at the page
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    member, created = Members.objects.get_or_create(user=request.user)
    # rank = Members.objects.filter(xp_points__gt=member.xp_points).count()+1
    # total_messages = Messages.objects.filter(Q(sender=request.user) | Q(reciever=request.user)).count()
    context = {'member': member}
    return render(request, 'accounts/profile.html', context)

@login_required
def updatemember(request):
    member = Members.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateMemberForm(instance=member)
    return render(request, 'accounts/edit_profile.html', {'form': form})
@login_required
def home(request):
    members = Members.objects.exclude(user=request.user)
    context = {
        'members': members
    }
    return render(request, 'accounts/home1.html', context)

@login_required
def chat(request, username):
    if request.user.username == username:
        return redirect('profile')

    reciever = get_object_or_404(User, username=username)
    
    # 1. Streak & XP Logic
    
    
    member = request.user.members
    

    # 2. POST Logic (Sending Messages/Media)
    if request.method == 'POST':
        
        # Pass request.FILES so the form can see the image/audio
        form = MessageForm(request.POST, request.FILES)
        
        # Check if it's a Voice Note (sent via JS fetch)
        audio_file = request.FILES.get('audio_file')

        if form.is_valid() or audio_file:
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.reciever = reciever
            
            # Manually attach audio if it came from the JS recorder
            if audio_file:
                msg.audio = audio_file
            
            # If you are NOT using fields in MessageForm for image/audio, 
            # you'd manually grab them here:
            if request.FILES.get('image_file'):
                msg.image = request.FILES.get('image_file')

            msg.save()

            # If AJAX (Voice Note), return JSON to avoid full page reload in background
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or audio_file:
                return JsonResponse({'status': 'success'})

            return redirect('chat', username=reciever.username)
    else:
        form = MessageForm()

    # 3. Retrieval Logic (Optimized)
    messages = Messages.objects.filter(
        (Q(sender=request.user, reciever=reciever) | Q(sender=reciever, reciever=request.user))
    ).order_by('timestamp')

    # 4. Mark Read Logic
    Messages.objects.filter(
        sender=reciever,
        reciever=request.user,
        is_read=False
    ).update(is_read=True)
    #perk = reciever.userperk_set.perk.name
    context = {
        'messages': messages, 
        'form': form, 
        'reciever': reciever,
        
    }
    return render(request, 'accounts/chat.html', context)