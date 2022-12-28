from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from . import forms, models


# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"


class UsersInventoryView(TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_dict'] = models.User.objects.all().order_by('first_name')
        return context


class UserDetailedView(DetailView):
    model = models.User
    template_name = 'per_user.html'
    context_object_name = 'user'


class AddNewUserView(CreateView):
    model = models.User
    form_class = forms.NewUser
    template_name = 'addUser.html'
    success_url = '/users/'


class UpdateUserView(UpdateView):
    model = models.User
    fields = '__all__'
    template_name = 'editUser.html'
    success_url = '/users/'


class DeleteUserView(DeleteView):
    model = models.User
    success_url = '/users/'
    template_name = 'confirm_delete.html'
