from .models import Userprofile
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver 

@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        Userprofile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_userprofile(sender, instance, **kwargs):
    instance.userprofile.save()