from django.shortcuts import render
from django.http import HttpResponse
import myApp.views


# Create your views here.
def index(request):
    return render(request, '../myApp/templates/index.html')

