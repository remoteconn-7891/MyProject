from django.urls import path
from arborfindr.views import index
from .views import homeowner_info, company_info, review_info, services_info
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import ArboristSearchView, autocomplete

app_name = 'arborfindr'

urlpatterns = [
path('search/', ArboristSearchView.as_view(), name='search_arborist'),
path('autocomplete/', autocomplete, name='autocomplete'),
path('register/', views.register, name = 'register'),
path('login/', views.user_login, name = 'login'),
path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
path('update_password/', views.update_password, name = 'update_password'),
path('homeowner_profile/', views.homeowner_profile, name = 'homeowner_profile'),
path('company_profile/', views.company_profile, name = 'company_profile'),
path('edit_homeowner_profile/', views.edit_homeowner_profile, name = 'edit_homeowner_profile'),
path('edit_company_profile/', views.edit_company_profile, name = 'edit_company_profile'),
path('arbor/review/', views.arbor_review, name='arbor_review'),
path('homeowner/', homeowner_info),
path('company/', company_info),
path('review_arbor/', review_info),
path('services/', services_info),
path('arborfindr/', index,),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)