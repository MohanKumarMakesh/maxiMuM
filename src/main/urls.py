# Django imports
'python function to use path in urls'
from django.urls import path
from .views import main, home, list_view, listing_view, edit_view, delete_view
# Url patterns
urlpatterns = [
    path('', main, name='main'),
    path('home/', home, name='home'),
    path('list/', list_view, name='list'),
    path('listing/<str:id>/', listing_view, name='listing'),
    path('listing/<str:id>/edit/', edit_view, name='edit'),
    path('listing/<str:id>/delete/', delete_view, name='delete'),
]   
 