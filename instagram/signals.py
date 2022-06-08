from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,Follow


user = User.objects.filter(username = 'charity').first()

@receiver(post_save,sender=User)
def create_profile(sender,instance,created ,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        # make new user follow admin in order to see posts in their timeline
        foll = Follow.objects.create(account = user ,follower= instance)
        foll.save()




@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()

# @receiver(post_save,sender=User)
# def save_follow(sender,instance,**kwargs):
#     instance.follower.save()
