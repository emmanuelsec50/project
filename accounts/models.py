from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, timedelta

# Create your models here.
class Members(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/a.png', blank=True, null=True)
    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)

class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recieved_messages')
    content = models.TextField(blank=True, null=True)
    audio = models.FileField(upload_to='voice_notes/', blank=True, null=True)
    image = models.ImageField(upload_to='chat_images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)
    is_anonymous = models.BooleanField(default=False)