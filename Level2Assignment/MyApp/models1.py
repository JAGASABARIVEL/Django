
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VehicleType(models.Model):
    vehicletype = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return str(self.vehicletype)

class Lorry(models.Model):
    vehicle = models.ForeignKey(VehicleType, on_delete=models.PROTECT)
    lorry_number = models.CharField(primary_key=True, max_length=75)
    year_model = models.IntegerField()
    def __str__(self):
        return str(self.lorry_number)

class Owner(models.Model):
    lorry = models.ForeignKey(Lorry, on_delete=models.PROTECT)
    ownerid = models.IntegerField(primary_key=True)
    ownername = models.CharField(max_length=264)
    def __str__(self):
        return str(self.ownername)

class Driver(models.Model):
    vehicle = models.ForeignKey(VehicleType, on_delete=models.PROTECT)
    driverid = models.IntegerField(primary_key=True)
    drivername = models.CharField(max_length=264)
    def __str__(self):
        return str(self.drivername)

class Booking(models.Model):
    bookingid = models.IntegerField(primary_key=True)
    lorryid = models.ForeignKey(Lorry, on_delete=models.CASCADE)
    driverid = models.ForeignKey(Driver, on_delete=models.CASCADE)
    bookingdate = models.DateTimeField(default=datetime.now)
    startdate = models.DateField()
    starttime = models.TimeField()
    enddate = models.DateField()
    endtime = models.TimeField()
    startkm = models.IntegerField()
    endkm = models.IntegerField()
    saleamount = models.IntegerField()
    dieselcost = models.IntegerField()
    tollcost = models.IntegerField()
    policecost = models.IntegerField()
    othercost = models.IntegerField()
    def __str__(self):
        return str(self.bookingid)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    user_blog = models.URLField(blank=True)
    user_image = models.ImageField(upload_to="user_image", blank=True)

    def __str__(self):
        return self.user.username
