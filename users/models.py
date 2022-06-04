from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    '''
    class profile for a user's personal profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_image',blank=True)
    name = models.CharField(max_length=50,blank=True)
    bio = models.CharField(max_length=150,blank=True)

    def __str__(self) -> str:
        return f'{self.user.username}'

    
    def save_profile(self):
        '''
        method to save a user's profile
        '''
        self.save()

    
    def delete_profile(self):
        '''
        method to delete a user's profile
        '''

        self.delete()




class Follow(models.Model):
    account = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'followers',default=0)
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'follower',default=0)

    def __str__(self) -> str:
        return f'{self.follower} following f{self.account}'

    def follow(self):
        self.save()

    def unfollow(self):
        self.delete()

    
    @classmethod
    def get_followers(cls, account_id):
        '''
        method to return a user's followers
        '''

        user = User.objects.filter(id = account_id)

        followers = user.followers.all()
        return followers

    @classmethod
    def get_following(cls,account_id):
        '''
        method to get all users that a user is following
        '''

        following = Follow.filter(account = account_id)

        return following






