from django.contrib import admin
from myApp import views
from django.urls import path

app_name = 'myApp'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('users/', views.UsersInventoryView.as_view(), name='users-inventory'),
    path('users/<int:pk>', views.UserDetailedView.as_view(), name='user-detail'),
    path('add_user/', views.add_user, name='add_user'),
]