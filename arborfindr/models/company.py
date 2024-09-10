from django.db import models
from .arborist_model import Arborist

# Create your models here.

class ArboristCompany(models.Model):
    arborist = models.ForeignKey(Arborist, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    company_size = models.CharField(max_length=30)

def __str__(self):
        return f'{self.company_name} ArboristCompany'

