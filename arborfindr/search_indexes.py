from haystack import indexes
from .models import Arborist


class ArboristIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    arborist_city = indexes.CharField(model_attr='city')
    arborist_state = indexes.CharField(model_attr='state')
    price = indexes.PositiveIntegerField()
    company_name = indexes.CharField(model_attr='company')
    one_star = indexes.PositiveIntegerField(default=0, null=True, blank=True)
    two_stars = indexes.PositiveIntegerField(default=0, null=True, blank=True)
    three_stars = indexes.PositiveIntegerField(default=0, null=True, blank=True)
    four_stars = indexes.PositiveIntegerField(default=0, null=True, blank=True)
    five_stars = indexes.PositiveIntegerField(default=0, null=True, blank=True)
    review_by_homeowner = indexes.CharField(model_attr='reviews')
    tree_pruning = indexes.CharField(model_attr='tree_pruning')
    tree_removal = indexes.CharField(model_attr='tree_removal')
    tree_planting = indexes.CharField(model_attr='tree_planting')
    pesticide_applications = indexes.CharField(model_attr='pesticide_applications')
    soil_management = indexes.CharField(model_attr='soil_management')
    tree_protection = indexes.CharField(model_attr='tree_protection')
    tree_risk_management = indexes.CharField(model_attr='tree_risk_management')
    tree_biology = indexes.CharField(model_attr='tree_biology')
    

    def get_model(self):
        return Arborist
    
    def prepare_arborist_cty(self, obj):
        return [arborist_city.id for arborist_city in obj.aborist_city_set.active().order_by('-created')]