import django_filters
from .models import Listing

class ListingFilter(django_filters.FilterSet):
    mileage = django_filters.NumberFilter(field_name='mileage', lookup_expr='lt')  

    class Meta:
        model = Listing
        fields = ['brand','transmission','mileage']


