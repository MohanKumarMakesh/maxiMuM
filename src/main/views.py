'function used to render the html file'
from django.shortcuts import render
# Create your views here.


def main(request):
    'return home page'
    return render(request, 'views/main.html')
