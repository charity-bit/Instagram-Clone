from re import template
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy



from django.contrib.auth.views import LoginView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .forms import RegistrationForm,CustomAuthForm


from .models import Follow, User,Post


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


def home(request):
    return  render(request,'instagram/timeline.html')



def profile(request,username):
    user = None
    full_user = None
    counted = None
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        user = User.objects.get(username = username)
        full_user = User.objects.filter(username = username).first()
        
    except User.DoesNotExist:
        print('user not found')

    count = len(Follow.objects.filter(account = user).exclude(follower = user))
    if count > 3:
        counted = count - 3
        
            
    context = {
        'posts': Post.objects.filter(user = user),
        'followers': Follow.objects.filter(account = user).exclude(follower = user), #get followers excluding the current user/ own account
        'following': Follow.objects.filter(follower = user).exclude(account = user),
        'notfollowing': Follow.objects.filter(follower = request.user,account = user),
        'username':user,
        'full_user':full_user,
        'counted':counted

    }  
    return render(request,'instagram/profile.html',context)




