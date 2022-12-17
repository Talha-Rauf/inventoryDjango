from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import User, AccessRecord
from . import forms


# Create your views here.
def index(request):
    return render(request, 'user_inv/index.html')


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}

    return render(request, 'user_inv/users.html', context=user_dict)


def per_User(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}

    return render(request, 'user_inv/per_user.html', context=user_dict)


def add_user(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESSFUL!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("COMPANY: " + form.cleaned_data['company'])

    return render(request, 'user_inv/addUser.html', {'form': form})
