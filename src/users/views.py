from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views import View
from .forms import UserForm, ProfileForm, LocationForm
from main.models import Listing
def login_view(request):
    'view to render login page'
    if request.method == 'POST':
        login_form = AuthenticationForm( request=request, data=request.POST)
        if login_form.is_valid():
            username  = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'views/login.html', {'login_form': login_form})
@login_required
def logout_view(request):
    'view to logout user'
    logout(request)
    return redirect('/')

class RegisterView(View):
    def get(self, request):
        'method to render the registration form'
        register_form = UserCreationForm()
        return render(request, 'views/register.html', {'register_form': register_form})
    def post(self, request):
        'method to register a new user'
        register_form = UserCreationForm( data=request.POST)
        if register_form.is_valid():
             user = register_form.save()
             user.refresh_from_db()
             login(request, user)
             messages.success(request, f'Welcome {user.username}!')
             return redirect('home')
        else:
            messages.error(request, 'Please retry registration')
            return render(request, 'views/register.html', {'register_form': register_form})
@method_decorator(login_required , name='dispatch')
class ProfileView(View):
    def get(self, request):
        'method to render the profile page'
        # Get the user's listings
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        location_form = LocationForm(instance=request.user.profile.location)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'location_form': location_form,
            'user_listings': user_listings,
        }
        return render(request, 'views/profile.html', context)
    
    def post(self, request):
        'method to update the profile'
        # Get the user's listings
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        location_form = LocationForm(request.POST, instance=request.user.profile.location)
        if user_form.is_valid() and profile_form.is_valid() and location_form.is_valid():
            user_form.save()
            profile_form.save()
            location_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating profile')
            return render(request, 'views/profile.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                'location_form': location_form,
                'user_listings': user_listings,
            })