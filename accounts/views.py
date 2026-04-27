from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from accounts.forms import UpdateMemberForm
from .models import Members, Messages
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