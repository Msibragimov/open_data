from django.db import models
from apps.customer.models import Customer

# Create your models here.


class ParkingZone(models.Model):
    number = models.IntegerField(unique=True)
    availble = models.BooleanField(default=True)


class BookingSpace(models.Model):
    counter = models.PositiveIntegerField(default=0, unique=True)
    customer = models.OneToOneField(Customer, on_delete=models.PROTECT)
    space = models.OneToOneField(ParkingZone, on_delete=models.PROTECT)
    time_counter = models.TimeField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)