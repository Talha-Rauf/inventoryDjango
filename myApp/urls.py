from django.contrib import admin
from myApp import views
from django.urls import path

urlpatterns = [
    path('', views.users, name='users'),
    path('per_user/', views.per_User, name='user'),
    path('add_user/', views.add_user, name='add_user'),
]