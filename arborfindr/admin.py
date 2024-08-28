from django.contrib import admin
from .models import HomeownerProfile
from .models import Homeowner, Arborist

# Register your models here.
admin.site.register(Homeowner)
admin.site.register(Arborist)
admin.site.register(HomeownerProfile)
