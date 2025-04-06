from django.contrib import admin
from .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    readonly_fields=('id','vin','created_at')
admin.site.register(Listing, ListingAdmin)
