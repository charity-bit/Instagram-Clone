from ctypes.wintypes import POINT
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from django import forms
from .models import Post

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')



class PostForm(forms.Model):
    class Meta:
        model = Post
        fields = ['image','post_name','post_caption']


