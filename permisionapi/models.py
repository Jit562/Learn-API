import email
from pyexpat import model
from django.db import models

# Create your models here.

# for use of signal user token create

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    mobile = models.IntegerField()
    desc = models.TextField()
    bool = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)



    
