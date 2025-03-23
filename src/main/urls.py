# Django imports
'python function to use path in urls'
from django.urls import path
from .views import main, home, list_view
# Url patterns
urlpatterns = [
    path('', main, name='main'),
    path('home/', home, name='home'),
    path('list/', list_view, name='list'),
]
