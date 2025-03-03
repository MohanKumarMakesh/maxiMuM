from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from localflavor.ie import IECountySelect, EircodeField


class Location(models.Model):
    'model to store location data'
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    county = IECountySelect()
    eircode = EircodeField()
    objects = models.Manager()


class Profile(models.Model):
    'model to store user data'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/photos', blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True)
    phone_no = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(
        Location, on_delete=models.CASCADE, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.user.username} Profile'
