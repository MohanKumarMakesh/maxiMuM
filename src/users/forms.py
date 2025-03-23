from django import forms

from .models import Location
from address.ie_counties import IE_COUNTY_CHOICES  
from address.forms import EircodeField 
class LocationForm(forms.ModelForm):
  county = forms.ChoiceField(required=True, choices=IE_COUNTY_CHOICES)
  eircode = forms.CharField(required=True, validators=[EircodeField().validators[0]])
  class Meta:
    model = Location
    fields = ['address_1', 'address_2', 'city', 'county', 'eircode']