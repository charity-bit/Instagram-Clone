from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    '''
    class profile for a user's personal profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_image',blank=True)
    followings = models.ManyToManyField(User,related_name='followings',blank=True)
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

class Post(models.Model):
    '''

    model for image's post
    '''
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    image = CloudinaryField('post_image',blank=True)
    like = models.ManyToManyField(User,related_name='likes',blank=True)
    post_name = models.CharField(max_length=50)
    post_caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 



    def __str__(self) -> str:
        return f'{self.post_name} - {self.post_caption}'

    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def search_post(cls,query):
        '''
        method to return searched posts
        '''
        posts = cls.objects.filter(name__icontains__ = query)
        return posts

    @classmethod
    def get_post_by_id(cls,id):
        '''
        method to search for post by id
        '''
        post = cls.objects.filter(id = id)

    @classmethod
    def get_user_posts(cls,user_id):
        '''
        method to return a user's posts
        '''

        # posts = cls.objects.filter(user = user_id)
        # return posts

        user = User.objects.filter(id = user_id).first()
        posts = user.posts.all()
        return posts

    @classmethod
    def get_posts(cls):
        '''
        method to return all posts
        '''

        posts = cls.objects.all()
        return posts

    
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    like = models.ManyToManyField(User,related_name='comment_likes',blank=True)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return f'{self.user.username} - {self.comment}'


    @classmethod
    def get_post_comments(cls,post_id):
        '''
        method to get comments related to a certain post
        '''

        comments = Comment.objects.filter(post = post_id)

        return comments

    def save_comment(self):

        '''
        instance method to save  a comment
        '''
        self.save()

    def delete_comment(self):
        '''
        method to delete comment
        '''

        self.delete()




    







