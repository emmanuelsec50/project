from django import forms
from django.shortcuts import render, redirect
from django.http import Http404
from .models import Members
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'firstapp/home.html')

@login_required
def room(request):
    pass

