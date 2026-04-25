from django.db import models

# Create your models here.
class Members(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
