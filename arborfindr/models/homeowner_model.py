from django.db import models

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
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=100)


     # Metadata for Homeowner Model
    class Meta:
        ordering = ['first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code']

    def __str__(self):
        return f'{self.first_name} Homeowner'



