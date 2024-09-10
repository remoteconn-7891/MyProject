from django.db import models
# Create your models here.

# Model Arborist
class Arborist(models.Model):
    arborist_city = models.CharField(max_length=30)
    arborist_state = models.CharField(max_length=30)
    years_experience = models.CharField(max_length=30)
    price = models.IntegerField(null='True')
    
    class Meta:
        ordering = ['arborist_city', 'arborist_state', 'years_experience', 'price']

    def __str__(self):
        return f'{self.arborist_city} Arborist'