# Django imports
'python function to use path in urls'
from django.urls import path
from .views import main, home
# Url patterns
urlpatterns = [
    path('', main, name='main'),
    path('home/', home, name='home')
]
