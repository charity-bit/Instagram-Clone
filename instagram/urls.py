from django.urls import path
from . import views

from .views import CustomLoginView

urlpatterns = [

    # user profile
    path('',CustomLoginView.as_view(),name='login'),
    path('register/',views.register,name = 'register'),
    path('timeline/',views.home,name='home'),

]