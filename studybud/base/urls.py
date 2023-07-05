from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('room/<str:pk>/', views.room, name = 'room'),
    
    path('create-room/', views.createRoom, name = 'createroom'),
    path('update-room/<str:pk>/', views.updateRoom, name = 'updateroom'),
    path('delete-room/<str:pk>/', views.deleteRoom, name = 'deleteroom'),
    
    path('login/', views.loginPage, name = 'login'),
]