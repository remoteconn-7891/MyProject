from django.db import models

from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

# Model Homeowner

class Homeowner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.PositiveIntegerField()
    bio = models.CharField(max_length=100, db_default='')
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
  

    # Metadata for Homeowner Model
    class Meta:
        ordering = ['first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'bio', 'profile_pic']


    def __str__(self):
        return f'{self.user.username} Homeowner'

    def save(self):
        super().save()

        # This opens the image
        img = Image.open(self.profile_pic.path)

        # Resizes image of profile
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            # Saves again
            img.save(self.profile_pic.path)

    


# Model Arborist
class Arborist(models.Model):
    business = models.CharField(max_length=30,
    blank=True, null=True)
    location = models.CharField(max_length=30)
    services_type = models.CharField(max_length=30)
    reviews = models.CharField(max_length=200)
    years_experience = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['business', 'location', 'services_type', 'reviews', 'price']

    def __str__(self):
        return f'{self.business} Arborist'
    