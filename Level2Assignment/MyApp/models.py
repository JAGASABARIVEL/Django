from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Places(models.Model):
    place = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.place

class SearchLorry(models.Model):
    loading_area = models.ForeignKey(Places, related_name='search_from', on_delete=models.CASCADE)
    unloading_area = models.ForeignKey(Places, related_name='search_to', on_delete=models.CASCADE)
    date_to_be_looked = models.DateField()

class BookState(models.Model):
    state = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.state

class VehicleType(models.Model):
    vehicletype = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return str(self.vehicletype)

class UserProfile(models.Model):
    LORRYOWNER = 'LO'
    DRIVER = 'DA'
    APPLICATION_OWNER = 'AO'
    MANAGER = 'MA'
    NORMALUSER = 'NU'
    USER_TYPE = ((LORRYOWNER, 'LORRYOWNER'),
                       (DRIVER, 'DRIVER'),
                       (APPLICATION_OWNER, 'APPLICATION_OWNER'),
                       (MANAGER, 'MANAGER'),
                       (NORMALUSER, 'NORMALUSER'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=260, blank=True)
    last_name = models.CharField(max_length=260, blank=True)
    password = models.CharField(max_length=260, blank=True)
    confirm_password = models.CharField(max_length=260, blank=True)
    phone = models.IntegerField(blank=True)
    confirm_phone = models.IntegerField(blank=True)
    user_type = models.CharField(choices=USER_TYPE, default=NORMALUSER, max_length=2)
    user_blog = models.URLField(blank=True)
    user_image = models.ImageField(upload_to="user_image", blank=True)
    def __str__(self):
        return self.user.username

class RegisterLorry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    lorry_number = models.CharField(primary_key=True, max_length=75)
    year_model = models.IntegerField()
    def __str__(self):
        return str(self.lorry_number)

class RegisterDriver(models.Model):
    name = models.CharField(max_length=260, primary_key=True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=260)
    referedby = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Booking(models.Model):
    lorryid = models.ForeignKey(RegisterLorry, on_delete=models.CASCADE)
    driverid = models.ForeignKey(RegisterDriver, on_delete=models.CASCADE)
    staginguser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staging_user', blank=True, null=True)
    bookinguser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_user', blank=True, null=True)
    bookingdate = models.DateTimeField(default=datetime.now)
    startdate = models.DateField()
    starttime = models.TimeField()
    enddate = models.DateField(blank=True, null=True)
    endtime = models.TimeField(blank=True, null=True)
    from_place = models.ForeignKey(Places, on_delete=models.CASCADE, related_name='booking_from_place')
    to_place = models.ForeignKey(Places, on_delete=models.CASCADE, related_name='booking_to_place')
    startkm = models.IntegerField(default=0)
    endkm = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=263, default="NEW")
    estimated_amount = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    dieselcost = models.IntegerField(blank=True, null=True)
    tollcost = models.IntegerField(blank=True, null=True)
    policecost = models.IntegerField(blank=True, null=True)
    othercost = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.id)
