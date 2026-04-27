from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.updatemember, name='edit'),
    path('register/', views.register, name='register'),
    path('chat/<str:username>', views.chat, name='chat'),
    path('chatlist/', views.chat_list, name='chatlist'),
    path('profileview/<str:username>/', views.profile_view, name='profile_view')
]