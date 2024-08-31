from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Homeowner


class UserForm(UserCreationForm):
   
   class Meta:
      model = User
      fields = [
         'username',
         'email',
         'password1',
         'password2',
      ]


class UpdateProfilePic(forms.ModelForm):
   class Meta:
      model = Homeowner
      fields = ['profile_pic']