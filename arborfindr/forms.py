from django import forms
from django.contrib.auth.models import User
from .models import HomeownerUser, ArboristCompany
from haystack.forms import SearchForm
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
   class Meta:
      model = User
      fields = (
         'email',
         'password',
      )

class HomeownerUserForm(forms.ModelForm):
   class Meta:
      model = HomeownerUser
      fields = ['bio', 'profile_pic']

class ArboristCompanyForm(forms.ModelForm):
   class Meta:
      model = ArboristCompany
      fields = ['company_name', 'company_logo']


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
