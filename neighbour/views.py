from django.shortcuts import render,redirect
from .models import Neighbourhood,Business,User,Profile

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):

    neighbourhood = Neighbourhood.objects.all()
    return render(request, 'home.html',locals())

