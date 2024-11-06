from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(signal=post_save, sender = User)
def create_profile(sender, instance, created, **kwargs) -> None:
    
    """
    This function creates a profile every time a new user is created
    """

    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender = User)
def save_profile(sender, instance, **kwargs) -> None:
    
    """
    This function saves the profile every time the user is saved
    """
    
    instance.profile.save()



