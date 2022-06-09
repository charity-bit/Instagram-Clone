from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from  django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



from django.contrib.auth.views import LoginView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import RegistrationForm,CustomAuthForm,PostForm



from .models import Follow, Profile, User,Post,Comment,Saved


# Create your views here.



@method_decorator(csrf_exempt,name='dispatch')
class CustomLoginView(LoginView):  #created custom loginView in order to use a different form class
    template_name = 'instagram/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    form_class = CustomAuthForm

    def get_success_url(self):
        return reverse_lazy('home')




@csrf_exempt
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
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

@login_required(login_url='/')
def home(request):
    following = Follow.objects.filter(follower = request.user).exclude(account = request.user)
    posts = Post.objects.all().order_by('-date_posted')
    saved_objects = Saved.objects.filter(user = request.user).order_by('-date_saved')
    post_followed = []
    saved_posts = []

    for post in posts:  #get all posts
        for follower in following:   #get all followings
            if post.user == follower.account:  #check if author in followers
                post_followed.append(post)

        for saved in saved_objects:
            if post.id == saved.post.id:
                saved_posts.append(post)

        
            
    context = {
        'posts':post_followed,
        'saved_p':saved_posts
    }
    return  render(request,'instagram/index.html',context)


@login_required(login_url='/')
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



    saved_objects = Saved.objects.filter(user = user).order_by('-date_saved')
    saved_p = []


    for post in Post.objects.all():
        for saved in saved_objects:
            if post.id == saved.post.id:
                saved_p.append(post)
        

    
    context = {
        'posts': Post.objects.filter(user = user).order_by('-date_posted'),
        'followers': Follow.objects.filter(account = user).exclude(follower = user), #get followers excluding the current user/ own account
        'following': Follow.objects.filter(follower = user).exclude(account = user),
        'notfollowing': Follow.objects.filter(follower = request.user,account = user),
        'saved_p':saved_p,
        'username':user,
        'full_user':full_user,
        'counted':counted

    }  
    return render(request,'instagram/profile.html',context)

@csrf_exempt
@login_required(login_url='/')
def follow(request):
    if request.method == 'POST':
        result = ''
        followers_list = []
        user_id = int(request.POST.get('user_id'))
        account = User.objects.get(pk=user_id)  

        if Follow.objects.filter(account=account, follower=request.user).exists():
            Follow.objects.filter(account=account, follower=request.user).delete()
            result = account.followers.count()
        else:
            foll_obj = Follow(account=account, follower=request.user)  
            foll_obj.save()

        followers =  Follow.objects.filter(account = account).exclude(follower = account)
        if followers:
            for follower in followers:
                followers_list.append(follower.follower.username)
              
            # if len(Follow.objects.filter(account=account, follower=request.user)) == 2:
            #     Follow.objects.filter(account=account, follower=request.user).first().delete()
        return  JsonResponse({'res':account.followers.count(),'list':followers_list})
    

@method_decorator(csrf_exempt,name='dispatch')
class AddpostView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'instagram/post_form.html'
    form_class = PostForm
    


    def get_success_url(self):
        return reverse_lazy('profile',kwargs={
            'username': self.request.user.username # on success edit return to profile page
        })


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddpostView,self).form_valid(form)
  

@login_required(login_url='/')
def save_comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        post = request.POST.get('post_id')

        post_ins = Post.objects.filter(id = post).first()
        user_ins = request.user

        comment = Comment(comment = comment,user = user_ins,post = post_ins)
        comment.save()

        return JsonResponse({'bool':True})

@login_required(login_url='/')
def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        data = 0
        id = int(request.POST.get('post')) # from profile.html ajax 
        post = get_object_or_404(Post,id=id)

        if post.like.filter(id = request.user.id).exists():
            post.like.remove(request.user)
            post.like_count -= 1
            data = 0
            result = post.like_count
            post.save()
        else:
            post.like.add(request.user)
            post.like_count += 1
            data = 1
            result = post.like_count
            post.save()
        
        return JsonResponse({'result':post.like.count(),'data':data})  # results passed to success function ajax


class UpdateProfile(LoginRequiredMixin,UpdateView):
    model = Profile
    fields = ['profile_pic','name','bio','phone_number','gender']
    template_name = 'instagram/edit_profile.html'


    # to limit people from editing other people's profile
    def get_queryset(self):
        base_qs = super(UpdateProfile,self).get_queryset()  # return queryset of Profile model
        return base_qs.filter(user=self.request.user)   #filter where user = current_user

    def get_success_url(self):
        return reverse_lazy('profile',kwargs={
            'username': self.request.user.username # on success edit return to profile page
        })

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateProfile,self).form_valid(form)

        

@login_required(login_url='/')
def search_user(request):
    full_user = None
    counted = None
    if 'username' in request.GET and request.GET['username']:
        query = request.GET.get('username')
        user = User.objects.filter(username__icontains=query).first()
        if user:
            full_user = User.objects.filter(username = user.username).first()
            count = len(Follow.objects.filter(account = user).exclude(follower = user))
            if count > 3:
                counted = count - 3
        # elif user is None:
        #     return HttpResponse('no such user')

       


    
        context = {
        'posts': Post.objects.filter(user = user).order_by('-date_posted'),
        # 'saved': saved,
        'followers': Follow.objects.filter(account = user).exclude(follower = user), #get followers excluding the current user/ own account
        'following': Follow.objects.filter(follower = user).exclude(account = user),
        'notfollowing': Follow.objects.filter(follower = request.user,account = user),
        'username':user,
        'full_user':full_user,
        'counted':counted
        }

        return render(request,'instagram/search.html',context)    
    else:
        message = 'you have not searches for anything'
        return render(request,'gallery/search.html',{'message':message})

class PostList(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'instagram/explore.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].all().order_by('-date_posted')
        return context 


    

class PostDetail(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post'
    template_name ='instagram/details.html'


def save_post(request):
    
    if request.method == 'GET':

        # get postid from the frontend
        post_id = request.GET.get('post_id')
        
         # state 
        state = 0


        # get user and post from the database
        post = Post.objects.get(id = post_id)
        user = User.objects.get(id = request.user.id)
        
        if Saved.objects.filter(user = user ,post = post).exists():
            Saved.objects.filter(user = user ,post = post).delete()

            state = 0
        else:
            saved_post = Saved(user = user,post = post)
            saved_post.save()
            state = 1
        return JsonResponse({'state':state})

    else:

        return HttpResponse('not a GET response')

    
