from django.urls import include, path
from . import views

urlpatterns=[
    path('home/'view.home,name='home')
]