from django.db import models


# Create your models here.
class User(models.Model):
    """user model,here we have a user details
    the name is unique"""
    user_name = models.CharField(max_length=250, unique=True, help_text="category name,name must be unique")



    def __str__(self):
        return self.user_name


class Driver(models.Model):
    """driver model,here we have a driver details
    the name is unique"""
    driver_name = models.CharField(max_length=250, unique=True, help_text="category name,name must be unique")


    def __str__(self):
        return self.driver_name


class Ride(models.Model):
    """ride model,this has a tree structure using foriegn key.
        """
    ride_requested = 'request'
    ride_accepted = 'accept'
    ride_done = 'done'

    ride_status_type = [
        (ride_requested, 'ride_requested'),
        (ride_accepted, 'ride_accepted'),
        (ride_done, 'ride_done')
    ]
    user_details = models.ForeignKey(User, on_delete=models.CASCADE)
    driver_details = models.ForeignKey(Driver, blank=True, null=True, on_delete=models.CASCADE)
    booking_start_time = models.DateTimeField(auto_now_add=True, help_text="ride start time")
    ride_status = models.CharField(max_length=8, choices=ride_status_type, default=ride_done, help_text="The current ride status")
