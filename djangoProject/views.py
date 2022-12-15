from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    my_dict = {'intro': "Please select the desired action from options given below:"}
    return render(request, 'user_inv/index.html', context=my_dict)

