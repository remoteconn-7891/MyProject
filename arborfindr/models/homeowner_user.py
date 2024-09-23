from django.db import models
from django.conf import settings
from.user import User

class HomeownerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='homeowner_user')
    homeowner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, db_default='')
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')