from django.test import TestCase
from . models import *

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    '''
    This is a class that perform unnittest  behaviour on the Image Model.
    '''
    def setUp(self):
        
        self.neighbourhood_one = Neighbourhood(name='bombklat',location='Alabama',description='good hood',occupants='23',health_tell='0623582825',police_number='991',neighbourhood_pic='images/lagoon.jpeg')

    def test_instance(self):
        Neighbourhood.objects.all().delete()
        self.assertTrue(isinstance(self.neighbourhood_one,Neighbourhood))

    def test_save_method(self):
        
        self.neighbourhood_one.save_neigbourhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(neigbourhoods) > 0)
     
    def tearDown(self):
        Neighbourhood.objects.all().delete()   

class BusinessTestClass(TestCase):
    '''
    This is a class that perform unnittest  behaviour on the Business Model.
    '''
    def setUp(self):
        self.business_one = Business(business_name='safaricom',business_email='safaricom@gmail.com',user="falone",neigbourhood='Alabama')

     def test_instance(self):
        self.assertTrue(isinstance(self.business_one,Business))

    def test_save_method(self):
        
        self.business_one.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def tearDown(self):
        Business.objects.all().delete()


    
class ProfileTestClass(TestCase):
    
    '''
    This is a class that perform unnittest  behaviour on the Profile Model.
    '''
    
    def setUp(self):
        self.profile_one = Profile(profile_pic='images/mine.jpg',bio='Currently doing datascience in moringa',user="falone",name='bombklat',location='Alabama',)

     def test_instance(self):
        self.assertTrue(isinstance(self.profile_one,Profile)) 

    def test_save_method(self):
        
        self.profile_one.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def tearDown(self):
        Profile.objects.all().delete()


        
       
        