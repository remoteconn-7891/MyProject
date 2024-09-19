from django.db import models
from .homeowner_model import Homeowner
from .homeowner_model import User
from django.conf import settings


class HomeownerUser(models.Model):
    homeowner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='homeowner_user')
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=100, db_default='')