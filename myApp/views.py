from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    my_dict = {'intro': "Please select the desired action from options given below:"}
    return render(request, 'user_inv/index.html', context=my_dict)


def users(request):
    my_dict = {'insert_me': "Hello I am from user_inv/views.py!",
               'test_1': "I am here to test out more template tags!",
               'test_2': "I am here for the same thing!"}
    return render(request, 'user_inv/users.html', context=my_dict)
