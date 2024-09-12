from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Homeowner
from haystack.forms import SearchForm


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

class CitySearchForm(SearchForm):
   find_city = forms.CharField(required=False)

   def search(self):
   # Store SearchQuerySet received from processing
      sqs = super(CitySearchForm, self).search()

      if not self.is_valid():
         return self.no_query_found()
      
      # Verify if find_city was chosen
      if self.cleaned_data['find_city']:
         sqs = sqs.filter(arborist_city__gte=self.cleaned_data['find_city'])