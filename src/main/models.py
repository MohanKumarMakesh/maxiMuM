import uuid
from django.db import models
from users.models import Profile
from .consts import CAR_BRANDS,TRANSMISSION_OPTIONS
from .utils import user_listing_path
# Create your models here.
class Listing(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
  brand = models.CharField(max_length=24,choices=CAR_BRANDS, default='none')
  model = models.CharField(max_length=24)
  vin = models.CharField(max_length=17)
  mileage = models.PositiveIntegerField(default=0)
  color = models.CharField(max_length=24)
  description = models.TextField()
  engine = models.CharField(max_length=24)
  transmission = models.CharField(max_length=24, choices=TRANSMISSION_OPTIONS)
  location = models.OneToOneField('users.Location', on_delete=models.SET_NULL, blank=True, null=True)
  image = models.ImageField(upload_to='listings/', blank=True, null=True)

  def __str__(self):
    return f'{self.seller.user.username}`s {self.model}'