from django import forms
from django.core import validators
from myApp.models import User


# def checkForValidName(value):
#    if value == int:
#        raise forms.ValidationError("NAME NEEDS TO BE LETTERS")


class NewUser(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
