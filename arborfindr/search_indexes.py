from haystack import indexes
from .models import ArboristCompany, ArboristReview, ServiceType


class ArboristCompanyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    company_name = indexes.CharField(model_attr='company_name')
    company_city = indexes.CharField(model_attr='company_city')
    company_state = indexes.CharField(model_attr='company_state')

    # Instead of directly indexing company_price, use the price_display method
    company_price_display = indexes.CharField(model_attr='price_display', null=True)  # Using the custom price_display method
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

class ServiceTypeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    # Update the fields to match the correct attribute names in the ServiceType model.
    # Assuming you want to index a `name` or similar attribute instead of the previous redundant ones.
    name = indexes.CharField(model_attr='name')  # Assuming the `ServiceType` model has a `name` attribute

    def get_model(self):
        return ServiceType

    def index_queryset(self, using=None):
        qs = self.get_model().objects.all()  # Get the queryset
        print(f'Indexing {qs.count()} ServiceType records')  # Print the count of records
        return qs
