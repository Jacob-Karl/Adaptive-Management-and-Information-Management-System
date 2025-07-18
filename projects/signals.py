from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Project)
def create_log(sender, instance, created, **kwargs):
    print("Signal Recieved")
    print(sender)
    print(instance)
    print(created)
    #print(instance.request.user)
    #if created:
    #    ChangeLog.objects.create(user=instance)

'''@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()'''