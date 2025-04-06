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
@login_required
def listing_view(request, id):
    try:
        print(id)
        listing = Listing.objects.get(id=id)
    except:
        messages.error(request, 'Listing does not exist')
        return redirect('home')
    return render(request, 'views/listing.html',{'listing': listing})

@login_required
def edit_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        if request.method == 'POST':
            listing_form = ListingForm(
                request.POST, request.FILES, instance=listing)
            location_form = LocationForm(
                request.POST, instance=listing.location)
            if listing_form.is_valid and location_form.is_valid:
                listing_form.save()
                location_form.save()
                messages.info(request, f'Listing {id} updated successfully!')
                return redirect('home')
            else:
                messages.error(
                    request, f'An error occured while trying to edit the listing.')
                return reload()
        else:
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)
        context = {
            'location_form': location_form,
            'listing_form': listing_form
        }
        return render(request, 'views/edit.html', context)
    except Exception as e:
        messages.error(
            request, f'An error occured while trying to access the edit page.')
        return redirect('home')
