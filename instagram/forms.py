from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from  django.contrib.auth.models import User
from django import forms
from .models import Post,Comment





class CustomAuthForm(AuthenticationForm):
     
    def __init__(self, *args, **kwargs):
        super(CustomAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'username'})
        self.fields['password'].widget.attrs.update({'placeholder':'password'})
        

    

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder':'email'})
        self.fields['username'].widget.attrs.update({'placeholder':'username'})
        self.fields['password1'].widget.attrs.update({'placeholder':'password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'confirm password'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'placeholder':'Add a comment...'})




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','post_caption']

    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['post_caption'].widget.attrs.update({'placeholder':'enter caption...'})



