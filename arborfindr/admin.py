from django.contrib import admin
from .models import Arborist, Homeowner

# Register your models here.
admin.site.register(Homeowner)
admin.site.register(Arborist)

