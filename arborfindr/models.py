from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import FieldDoesNotExist

from PIL import Image

# Create your models here.

# Model Homeowner
class Homeowner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.PositiveIntegerField()

    def __str__(self):
# String that represents Homeowner object
        return self.first_name
    
# Metadata
class Meta:
    ordering = ['first_name', 'last_name', 'street_address', 'city', 'state']
    
 # Model user (homeowner) profile class
class HomeownerProfile(models.Model):
    username = models.CharField(max_length=30)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=200)
    homeowner=models.ForeignKey(Homeowner, on_delete=models.CASCADE)

    def __str__(self):
# String that represents Homeowner profile object
        return self.username
    
    # Metadata
class Meta:
    ordering = ['username', 'profile_pic', 'bio']

# Model Arborist
class Arborist(models.Model):
    business = models.CharField(max_length=30,
        blank=True, null=True)
    location = models.CharField(max_length=30)
    services_type = models.CharField(max_length=30)
    reviews = models.CharField(max_length=200)
    years_experience = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    
def __str__(self):
    return self.business

class Meta:
    ordering = ['business', 'location', 'services_type', 'reviews', 'price']
