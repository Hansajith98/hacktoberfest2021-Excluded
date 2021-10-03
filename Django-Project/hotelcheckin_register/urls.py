from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.hotel_form,name='hotel_insert'), # get and post req. for insert operation
    path('<int:id>/', views.hotel_form,name='hotel_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.hotel_delete,name='hotel_delete'),
    path('list/',views.hotel_list,name='hotel_list') # get req. to retrieve and display all records
]