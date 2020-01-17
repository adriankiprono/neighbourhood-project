from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):

    neighbourhood = Neighbourhood.objects.all()
    return render(request, 'home.html',locals())