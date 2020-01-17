from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    name=models.CharField(max_length=30,null=True)
    location=models.CharField(max_length=40,null=True)
    occupants=models.PositiveIntegerField(null=True)




