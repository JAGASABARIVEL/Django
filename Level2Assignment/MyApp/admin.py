from django.contrib import admin
from MyApp.models import (VehicleType, RegisterLorry,
                          Booking, UserProfile,
                          Places, BookState,
                          SearchLorry)
# Register your models here.
admin.site.register(VehicleType)
admin.site.register(RegisterLorry)
admin.site.register(Booking)
admin.site.register(Places)
admin.site.register(BookState)
admin.site.register(UserProfile)
admin.site.register(SearchLorry)
