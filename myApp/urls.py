from django.contrib import admin
from myApp import views
from django.urls import path

app_name = 'myApp'

urlpatterns = [
    path('index/', views.HomePageView.as_view(), name='index'),
    path('users/', views.UsersInventoryView.as_view(), name='users-inventory'),
    path('users/<int:pk>', views.UserDetailedView.as_view(), name='user-detail'),
    # path('users/editUser/<int:pk>', views.EditUserDetail.as_view(), name='edit-user-detail'),
    path('add_user/', views.AddNewUserView.as_view(), name='add-user'),
]