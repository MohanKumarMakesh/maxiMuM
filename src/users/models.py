from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from localflavor.ie.forms import IECountySelect, EircodeField
from users.utils import user_directory_path


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
    photo = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True)
    phone_no = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(
        Location, on_delete=models.SET_NULL, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.user.username} Profile'
