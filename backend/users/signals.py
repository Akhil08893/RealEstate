from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile
from django.db.models.signals import post_save

user =get_user_model()


@receiver(post_save,sender=user)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(seller = instance)
        
        
@receiver(post_save,sender =user)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
