from django.shortcuts import render,redirect
from .models import Neighbourhood,Business,User,Profile

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):

    neighbourhood = Neighbourhood.objects.all()
    return render(request, 'home.html',locals())

def search_results(request):
    
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_business_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-hood/search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-hood/search.html',{"message":message})

