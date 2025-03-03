# Django imports
'python function to use path in urls'
from django.urls import path
from .views import home
urlpatterns = [
    path('', home, name='home'),
]
