from django.contrib.auth import get_user_model
from django.contrib import admin
from .models import Homeowner, Arborist, ArboristReview, ServiceType, ArboristCompany

# Get the user model
User = get_user_model()
admin.site.register(User)

# Register your models here.

@admin.register(Homeowner)
class HomeownerAdmin(admin.ModelAdmin):
    list_display = ('bio', 'profile_pic')  # Adjust fields as per your model

@admin.register(Arborist)
class ArboristAdmin(admin.ModelAdmin):
    list_display = ('arborist_city', 'arborist_state', 'years_experience', 'price')  # Adjust as per your model fields

@admin.register(ArboristReview)
class ArboristReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'review_text', 'reviewed_on')

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Single field `name` for service types

@admin.register(ArboristCompany)
class ArboristCompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_logo', 'company_city', 'company_state', 'experience', 'price_display')  # Use price_display here
    filter_horizontal = ('services',)

    # Add many-to-many fields for display if needed
  # Add a horizontal filter widget for many-to-many relationships



