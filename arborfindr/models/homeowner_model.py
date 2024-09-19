from django.db import models
from django.contrib.auth.models import AbstractUser


from PIL import Image


# Create your models here.

# Model Homeowner
class User(AbstractUser):
    email = models.EmailField('Email Address', unique=True)
    role = models.CharField(max_length=1, choices=[('c', 'Company'),
                                                   ('h', 'Homeowner')])

class Homeowner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.PositiveIntegerField()


     # Metadata for Homeowner Model
    class Meta:
        ordering = ['first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code']

    def __str__(self):
        return f'{self.first_name} Homeowner'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # This opens the image of profile page
        img = Image.open(self.profile_pic.path)

        # Resizes image of profile picture
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            # Saves again
            img.save(self.profile_pic.path)

