from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    ROLE_CHOICES = (
        ('homeowner', 'Homeowner'),
        ('company', 'Company'),
    )
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
