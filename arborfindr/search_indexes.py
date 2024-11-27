from haystack import indexes
from .models import ArboristCompany, ArboristReview, ServicesType


class ArboristCompanyIndex(indexes.SearchIndex, indexes.Indexable): 
    text = indexes.EdgeNgramField(document=True, use_template=True)
    company_name = indexes.CharField(model_attr='company_name')
    company_city = indexes.CharField(model_attr='company_city')
    company_state = indexes.CharField(model_attr='company_state')
    company_price = indexes.IntegerField(model_attr='company_price', null=True)
    experience = indexes.CharField(model_attr='experience')

    def start_review(self, obj):
        return [review.review_text for review in obj.arboristreview_set.all()]
    def get_model(self):
        return ArboristCompany

    def index_queryset(self, using=None):
        qs = self.get_model().objects.all()  # Get the queryset
        print(f'Indexing {qs.count()} Arborist records')  # Print the count of records
        return qs


class ArboristReviewIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    one_star = indexes.IntegerField(model_attr='one_star', default=0, null=True)  # corrected
    two_stars = indexes.IntegerField(model_attr='two_stars', default=0, null=True)  # corrected
    three_stars = indexes.IntegerField(model_attr='three_stars', default=0, null=True)  # corrected
    four_stars = indexes.IntegerField(model_attr='four_stars', default=0, null=True)  # corrected
    five_stars = indexes.IntegerField(model_attr='five_stars', default=0, null=True)  # corrected
    review_by_homeowner = indexes.CharField(model_attr='reviews_by_homeowner')

    def get_model(self):
        return ArboristReview

    def index_queryset(self, using=None):
        qs = self.get_model().objects.all()  # Get the queryset
        print(f'Indexing {qs.count()} ArboristReviews records')  # Print the count of records
        return qs

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
        qs = self.get_model().objects.all()  # Get the queryset
        print(f'Indexing {qs.count()} ServicesType records')  # Print the count of records
        return qs
