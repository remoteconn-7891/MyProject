
from django.contrib.auth import get_user_model
from django.contrib import admin
from .models import Homeowner
from .models import Arborist
from .models import ArboristReview
from .models import ServicesType
from .models import ArboristCompany


User = get_user_model()
admin.site.register(User)

# Register your models here.

@admin.register(Homeowner)
class HomeownerAdmin(admin.ModelAdmin):
    list_display = ('bio', 'profile_pic')

@admin.register(Arborist)
class ArboristAdmin(admin.ModelAdmin):
    list_display = ('arborist_city', 'arborist_state', 'years_experience', 'price')  # Adjust as per your model fields

@admin.register(ArboristReview)
class ArboristReviewAdmin(admin.ModelAdmin):
    list_display = ( 'rating', 'review_text', 'reviewed_on')

@admin.register(ServicesType)
class ServicesTypeAdmin(admin.ModelAdmin):
    list_display = ('tree_pruning', 'tree_removal', 'tree_planting', 'pesticide_applications', 'soil_management',
                    'tree_protection', 'tree_risk_management', 'tree_biology')

@admin.register(ArboristCompany)
class ArboristCompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_logo')


