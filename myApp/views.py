from django.shortcuts import render
from django.utils import timezone
from myApp.models import User, AccessRecord
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from . import forms


# Create your views here.
class HomePageView(TemplateView):

    template_name = "user_inv/index.html"


class UsersInventoryView(TemplateView):

    template_name = "user_inv/users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_dict'] = User.objects.all().order_by('first_name')
        return context


class UserDetailedView(DetailView):

    queryset = User.objects.all()

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj


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
