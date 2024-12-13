from rest_framework import serializers
from .models import ArboristReview, ArboristCompany, Homeowner, ServiceType


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id', 'name']


class ArboristCompanySerializer(serializers.ModelSerializer):
    services = ServiceTypeSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ArboristCompany
        fields = '__all__'

class HomeownerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeowner
        fields = '__all__'


class ArboristReviewSerializer(serializers.ModelSerializer):
    arborist_company = serializers.PrimaryKeyRelatedField(queryset=ArboristCompany.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Homeowner.objects.all())

    class Meta:
        model = ArboristReview
        fields = '__all__'

