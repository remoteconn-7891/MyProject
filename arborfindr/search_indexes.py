from haystack import indexes
from .models import Arborist, ArboristCompany, ArboristReview, ServicesType


class ArboristIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    arborist_city = indexes.CharField(model_attr='arborist_city')
    arborist_state = indexes.CharField(model_attr='arborist_state')
    price = indexes.IntegerField(model_attr='price', null='True')

    def get_model(self):
        return Arborist
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ArboristCompanyIndex(indexes.SearchIndex, indexes.Indexable): 
    text = indexes.EdgeNgramField(document=True, use_template=True)
    company_name = indexes.CharField(model_attr='company')

    def get_model(self):
        return ArboristCompany
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ArboristReviewIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    one_star = indexes.IntegerField(model_attr='one_star', default=0, null=True, blank=True)
    two_stars = indexes.IntegerField(model_attr='two_stars', default=0, null=True, blank=True)
    three_stars = indexes.IntegerField(model_attr='three_stars', default=0, null=True, blank=True)
    four_stars = indexes.IntegerField(model_attr='four_stars', default=0, null=True, blank=True)
    five_stars = indexes.IntegerField(model_attr='five_stars', default=0, null=True, blank=True)
    review_by_homeowner = indexes.CharField(model_attr='reviews_by_reviewes')

    def get_model(self):
        return ArboristReview
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ServicesTypeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    tree_pruning = indexes.CharField(model_attr='tree_pruning')
    tree_removal = indexes.CharField(model_attr='tree_removal')
    tree_planting = indexes.CharField(model_attr='tree_planting')
    pesticide_applications = indexes.CharField(model_attr='pesticide_applications')
    soil_management = indexes.CharField(model_attr='soil_management')
    tree_protection = indexes.CharField(model_attr='tree_protection')
    tree_risk_management = indexes.CharField(model_attr='tree_risk_management')
    tree_biology = indexes.CharField(model_attr='tree_biology')

    def get_model(self):
        return ServicesType
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
    