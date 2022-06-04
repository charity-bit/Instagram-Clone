from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_image')
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self) -> str:
        return f'{self.user.username}'



class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    image = CloudinaryField('post_image',blank=True)
    post_name = models.CharField(max_length=50)
    post_caption = models.TextField()


    def __str__(self) -> str:
        return f'{self.post_name} - {self.post_caption}'



class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')


    def __str__(self) -> str:
        return f'{self.user.username} - {self.comment}'

    

class Follow(models.Model):
    account = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'followers',default=0)
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'follower',default=0)

    def __str__(self) -> str:
        return f'{self.follower}'










