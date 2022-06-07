from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

from .views import CustomLoginView,AddpostView,UpdateProfile

urlpatterns = [

    # user login
    path('',CustomLoginView.as_view(),name='login'),
    path('register/',views.register,name = 'register'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),

    # profile
    path('profile/<str:username>/',views.profile,name='profile'),
    path('add-comment/',views.save_comment,name='comment'),
    path('add-like/',views.like,name='like'),
    path('follow/',views.follow,name='follow'),
    path('profile/<int:pk>/edit/',UpdateProfile.as_view(),name='update-profile'),


    # posts
    path('post/',AddpostView.as_view(),name='post'),
    path('timeline/',views.home,name='home'),
    path('search/',views.search_user,name='search')

]