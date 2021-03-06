from django.contrib import admin
from .models import User, Driver, Ride


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', )


admin.site.register(User, UserAdmin)


class DriverAdmin(admin.ModelAdmin):
    list_display = ('driver_name', )


admin.site.register(Driver, DriverAdmin)


class RideAdmin(admin.ModelAdmin):
    list_display = ('ride_status','user_details', 'driver_details', 'booking_start_time')


admin.site.register(Ride, RideAdmin)
