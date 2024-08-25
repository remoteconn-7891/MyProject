import django_filters
from .models import Arborist

# Arborist viewset function with filter functions
class ArboristFilter(django_filters.FilterSet):
    class Meta:
        model = Arborist
        fields = ['services_type', 'reviews', 'years_experience', 'price']