from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import Inventory, User, AccessRecord


# Create your views here.

def index(request):
    my_dict = {'intro': "Please select the desired action from options given below:"}

    return render(request, 'user_inv/index.html', context=my_dict)


def users(request):
    user_list = User.objects.order_by('name')
    name_dict = {'user_inventory': user_list}

    return render(request, 'user_inv/users.html', context=name_dict)
