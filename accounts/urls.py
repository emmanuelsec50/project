from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.updatemember, name='edit'),
    path('register/', views.register, name='register'),
    path('chat/<str:username>', views.chat, name='chat')
]