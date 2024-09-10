from django.db import models
from .arborist_model import Arborist

# Model ArboristServiceType here

class ServicesType(models.Model):
    arborist = models.ForeignKey(Arborist, on_delete=models.CASCADE)
    tree_pruning = models.CharField(max_length=30)
    tree_removal = models.CharField(max_length=30)
    tree_planting = models.CharField(max_length=30)
    pesticide_applications = models.CharField(max_length=30)
    soil_management = models.CharField(max_length=30)
    tree_protection = models.CharField(max_length=30)
    tree_risk_management = models.CharField(max_length=30)
    tree_biology = models.CharField(max_length=30)

        # Metadata for ArboristReview Models

    def __str__(self):
        return f'{self.tree_pruning} ServicesType'
