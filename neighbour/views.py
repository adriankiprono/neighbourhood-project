from django.shortcuts import render,redirect
from .models import Neighbourhood,Business,User,Profile
from django.http import HttpResponse,Http404
from .forms import NewHoodForm
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


@login_required(login_url='/accounts/login/')
def neighbourhood(request,neighbourhood_id):
    try:
        neigbourhood = Neighbourhood.objects.get(id = Neighbourhood_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-hood/hood.html", locals())

@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewHoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.profile = current_user
            neighbourhood.save()
        return redirect('home')

    else:
        form = NewHoodForm()
    return render(request, 'all-hood/new_hood.html', {"form": form})
