'function used to render the html file'
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def main(request):
    'return main page'
    return render(request, 'views/main.html')
@login_required
def home(request):
    'return home page'
    return render(request, 'views/home.html')