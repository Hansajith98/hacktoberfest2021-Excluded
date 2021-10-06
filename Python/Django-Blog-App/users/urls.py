from django.contrib.auth.models import User
from django.urls import path
from . import views
import blog

urlpatterns=[
    path('', blog.views.blogPage),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.userProfile, name='profile')
]