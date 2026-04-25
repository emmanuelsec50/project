from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('home/room/<str:i>/', views.room, name='room'),
    # path('test/', views.test, name='test'),
    #path('', views.register, name='register' ),
]