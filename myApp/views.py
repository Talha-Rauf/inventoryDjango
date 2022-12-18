from django.shortcuts import render
# from django.http import HttpResponse
from myApp.models import User, AccessRecord
from . import forms


# Create your views here.
def index(request):

    if request.method == 'GET':
        return users(request)

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
    form = forms.NewUser()

    if request.method == 'POST':
        form = forms.NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("VALIDATION SUCCESSFUL!")
            # print("NAME: " + form.cleaned_data['first_name' + ' ' + 'second_name'])
            # print("EMAIL: " + form.cleaned_data['email'])
            # print("COMPANY: " + form.cleaned_data['company'])
            return index(request)
        else:
            print("ERROR FORM INVALID")

    return render(request, 'user_inv/addUser.html', {'form': form})
