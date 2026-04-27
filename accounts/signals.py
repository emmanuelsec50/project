from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Members

@receiver(post_save, sender=User)
def create_member(sender, instance, created, **kwargs):
    if created:
        Members.objects.create(user=instance)