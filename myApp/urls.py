from django.contrib import admin
from myApp import views
from django.urls import path

urlpatterns = [
    path('', views.users, name='users'),
]