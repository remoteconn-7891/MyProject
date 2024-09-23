from django.db import models
from django.conf import settings
from.user import User


# Create your models here.

class ArboristCompany(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='arborist_company')
    arborist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    company_logo = models.ImageField(upload_to='company_logo', blank=True)

def __str__(self):
        return f'{self.company_name} ArboristCompany'

