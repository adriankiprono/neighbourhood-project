from .models import *
from django import forms
class NewHoodForm(forms.ModelForm):
    class Meta:
        model= Neighbourhood
        fields=['profile','name','location','description','occupants','health_tell','police_number','neighbourhood_picture']
