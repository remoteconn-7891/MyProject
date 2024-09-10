from django.urls import path
from arborfindr.views import index
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.urls import include, re_path
from .views import profile


urlpatterns = [
re_path(r'^search/', include('haystack.urls')),
path('register/', views.register, name = 'register'),
path('login/', views.user_login, name = 'login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# URL paths for updating password
path('update_password/', views.update_password, name = 'update_password'),
path('profile/', views.profile, name ='user_profile'),
path('', index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)