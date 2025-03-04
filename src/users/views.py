from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def login_view(request):
    'view to render login page'
    login_form = AuthenticationForm()
    return render(request, 'views/login.html', {'form': login_form})
