from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import User, AccessRecord


# Create your views here.
def index(request):
    return render(request, 'user_inv/index.html')


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}

    return render(request, 'user_inv/users.html', context=user_dict)
