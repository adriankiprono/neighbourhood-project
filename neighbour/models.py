from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Neighbourhood(models.Model):
    name=models.CharField(max_length=40,null=True)
    location=models.CharField(max_length=40,null=True)
    description = models.TextField(max_length=400,null=True)
    occupants=models.PositiveIntegerField(null=True)
    health_tell = models.CharField(max_length=12,null=True, blank=True)
    police_number = models.CharField(max_length=12,null=True, blank=True)
    neighbourhood_picture = models.ImageField(upload_to='avatar/', default='default.jpg')
    profile=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post = models.TextField(null=True)

    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
    

class User(models.Model):
    user_name=models.CharField(max_length=50,null=True)
    user_id =models.AutoField(primary_key=True)
    email=models.EmailField(max_length=100,null=True)
    neighbourhood=models.ForeignKey('Neighbourhood',on_delete=models.CASCADE,)
    

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['user_name']

class Business(models.Model):
    business_name=models.CharField(max_length=50,null=True)
    business_email=models.EmailField(max_length=100,null=True)
    neighbourhood=models.ForeignKey('Neighbourhood',on_delete=models.CASCADE,)
    user=models.ForeignKey('User',on_delete=models.CASCADE,)

    @classmethod
    def search_by_business_name(cls,search_term):
        business=cls.objects.filter(business_name__icontains=search_term)
        return business


    def __str__(self):
        return self.business_name

    class Meta:
        ordering = ['business_name']

class Profile(models.Model):
    profile_name= models.CharField(max_length=255,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')












