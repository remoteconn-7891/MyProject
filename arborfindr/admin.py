from django.contrib import admin
from .models import Homeowner
from .models import Arborist
from .models import ArboristReview
from .models import ServicesType
from .models import ArboristCompany

# Register your models here.

admin.site.register([Homeowner])
admin.site.register([Arborist])
admin.site.register([ArboristReview])
admin.site.register([ServicesType])
admin.site.register([ArboristCompany])


