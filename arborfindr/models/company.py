from django.db import models
from django.conf import settings
from .type_service_model import ServiceType  # Import ServiceType model

class ArboristCompany(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='arborist_company')
    arborist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=40)
    company_logo = models.ImageField(upload_to='company_logo', blank=True)
    company_city = models.CharField(max_length=70, default="")
    company_state = models.CharField(max_length=40, default="")
    experience = models.CharField(max_length=50, default="")
    company_price = models.IntegerField(null=True)  # Optionally keep this, or switch to a CharField
    services = models.ManyToManyField(ServiceType, related_name='companies', blank=True)  # Services field

    def __str__(self):
        return f'{self.company_name} ArboristCompany'

    def price_display(self):
        if self.company_price:
            return f"${self.company_price}"
        else:
            return "Request a price estimate"

    price_display.short_description = 'Price/Estimate'  # This will show as the header in the admin interface

