'function used to render the html file'
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ListingForm
from users.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter
# Create your views here.

from .models import Listing
def main(request):
    'return main page'
    return render(request, 'views/main.html')
@login_required
def home(request):
    'return home page'
    listing = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listing)
    context = {'filter': listing_filter}
    return render(request, 'views/home.html', context)

@login_required
def list_view(request):
    'return list page'
    if request.method == 'POST':
        try:
            form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST)
            if form.is_valid() and location_form.is_valid():
                listing = form.save(commit=False)
                listing.seller = request.user.profile
                location = location_form.save()
                listing.location = location
                listing.save()
                messages.success(request, 'Listing created successfully')
                return redirect('home')

        except:
            print('Error')
            raise Exception('Error')
            messages.error(request, 'Error')  

    elif request.method == 'GET':
        form = ListingForm()
        location_form = LocationForm()
        return render(request, 'views/list.html', {'form': form, 'location_form': location_form})
    