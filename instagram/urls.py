from django.urls import path
from . import views

from .views import CustomLoginView

urlpatterns = [

    # user login
    path('',CustomLoginView.as_view(),name='login'),
    path('register/',views.register,name = 'register'),

    # profile
    path('<str:username>/',views.profile,name='profile'),




    path('timeline/',views.home,name='home'),

]