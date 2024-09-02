from django.db import models
# Create your models here.

# Model Arborist
class Arborist(models.Model):
    company = models.CharField(max_length=30, blank=True, null=True)
    services_type = models.CharField(max_length=30)
    reviews = models.CharField(max_length=200)
    arborist_city = models.CharField(max_length=30)
    arborist_state = models.CharField(max_length=30)
    years_experience = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['company', 'services_type', 'reviews', 'arborist_city', 'arborist_state', 'years_experience', 'price']

    def __str__(self):
        return f'{self.business} Arborist'