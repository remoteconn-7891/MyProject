from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Homeowner


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Homeowner.objects.create(user=instance)


@receiver(post_save, sender=User)
def update_profile(sender, instance, **kwargs):
    instance.homeowner.save()