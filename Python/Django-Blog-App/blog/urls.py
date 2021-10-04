from django.urls import path
from . import views

urlpatterns = [
   path('', views.blogPage, name='blog'),
   path('content/<str:pk>/', views.blogContent, name='blog-content'),
   path('create-post/', views.createPost, name='create-post'),
   path('edit-post/<str:pk>', views.updatePost, name='edit-post'),
   path('delete-post/<str:pk>', views.deletePost, name='delete-post')
]
