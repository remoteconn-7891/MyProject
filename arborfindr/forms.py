from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Homeowner, ArboristCompany
from haystack.forms import SearchForm


class UserForm(UserCreationForm):
   
   class Meta:
      model = User
      fields = (
         'email',
         'password',
      )



class UpdateProfilePic(forms.ModelForm):
   class Meta:
      model = Homeowner
      fields = ('profile_pic')

class HomeownerForm(forms.ModelForm):
   class Meta:
      model = Homeowner
      fields = ('first_name',
                'last_name',
                'street_address',
                'city',
                'state',
                'zip_code')

class CompanyForm(forms.ModelForm):
   class Meta:
      model = ArboristCompany
      fields = ('company_name')

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