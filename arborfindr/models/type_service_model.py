from django.db import models

# Model for Service Types
class ServiceType(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., "Tree Pruning", "Tree Removal"

    def __str__(self):
        return self.name


