from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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