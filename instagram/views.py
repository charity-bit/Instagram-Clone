from multiprocessing import context
from re import template
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from  django.views.generic import CreateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator



from django.contrib.auth.views import LoginView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import RegistrationForm,CustomAuthForm,PostForm



from .models import Follow, User,Post,Comment


# Create your views here.


@method_decorator(csrf_exempt,name='dispatch')
class CustomLoginView(LoginView):
    template_name = 'instagram/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    form_class = CustomAuthForm

    def get_success_url(self):
        return reverse_lazy('home')





def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
        
    else: 

        form = RegistrationForm()

    context = {
        'form':form
        }

    return render(request,'instagram/register.html',context)

# \\timeline
def home(request):
    following = Follow.objects.filter(follower = request.user).exclude(account = request.user)
    posts = Post.objects.all().order_by('-date_posted')
    post_followed = []

    for post in posts:  #get all posts
        for follower in following:   #get all followings
            if post.user == follower.account:  #check if author in followers
                print(post.user)
                post_followed.append(post)
            
    context = {
        'posts':post_followed
    }
    return  render(request,'instagram/index.html',context)



def profile(request,username):
    user = None
    full_user = None
    counted = None
    if not request.user.is_authenticated:
        return redirect('login')
   
    user = get_object_or_404(User,username = username)
    full_user = User.objects.filter(username = username).first()
        
    
    count = len(Follow.objects.filter(account = user).exclude(follower = user))
    if count > 3:
        counted = count - 3
        
            
    context = {
        'posts': Post.objects.filter(user = user).order_by('-date_posted'),
        'followers': Follow.objects.filter(account = user).exclude(follower = user), #get followers excluding the current user/ own account
        'following': Follow.objects.filter(follower = user).exclude(account = user),
        'notfollowing': Follow.objects.filter(follower = request.user,account = user),
        'username':user,
        'full_user':full_user,
        'counted':counted

    }  
    return render(request,'instagram/profile.html',context)

@csrf_exempt
def follow(request):
    if request.method == 'POST':
        result = ''
        user_id = int(request.POST.get('user_id'))
        account = User.objects.get(pk=user_id)  

        if Follow.objects.filter(account=account, follower=request.user).exists():
            Follow.objects.filter(account=account, follower=request.user).delete()
            result = account.followers.count()
        else:
            foll_obj = Follow(account=account, follower=request.user)  
            foll_obj.save() 
            result = account.followers.count()

        return  JsonResponse({'result':result})
        
    



@method_decorator(csrf_exempt,name='dispatch')
class AddpostView(CreateView):
    model = Post
    template_name = 'instagram/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddpostView,self).form_valid(form)
  


def save_comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        post = request.POST['post']

        post_ins = Post.objects.filter(id = post).first()
        user_ins = request.user

        comment = Comment(comment = comment,user = user_ins,post = post_ins)
        comment.save()

        return JsonResponse({'bool':True})

def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('post'))
        post = get_object_or_404(Post,id=id)

        if post.like.filter(id = request.user.id).exists():
            post.like.remove(request.user)
            post.like_count -= 1
            result = post.like_count
            post.save()
        else:
            post.like.add(request.user)
            post.like_count += 1
            result = post.like_count
            post.save()
        # print(result)
        return JsonResponse({'result':result,})



    




