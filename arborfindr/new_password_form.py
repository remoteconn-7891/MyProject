from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserForm(UserCreationForm):
   
   class Meta:
      model = User
      fields = [
         'username',
         'email',
         'password1',
         'password2',
      ]

class UpdateProfileForm(forms.ModelForm):
   username = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control-file'}))
   profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
   bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control-file'}))
