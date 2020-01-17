from django.db import models


# Create your models here.
class User(models.Model):
    """user model,here we have a user details
    the name is unique"""
    user_name = models.CharField(max_length=250, unique=True, help_text="category name,name must be unique")
    mobile_number = models.CharField(max_length=10, help_text="enter your mobile number")
    booking_start_time = models.DateTimeField(auto_now_add=True, help_text="ride start time")
    booking_end_time = models.DateTimeField(auto_now=True, help_text="ride end time")

    def __str__(self):
        return self.user_name


class Driver(models.Model):
    """driver model,here we have a driver details
    the name is unique"""
    driver_name = models.CharField(max_length=250, unique=True, help_text="category name,name must be unique")
    mobile_number = models.CharField(max_length=10, help_text="enter your mobile number")
    booking_start_time = models.DateTimeField(auto_now_add=True, help_text="ride start time")
    booking_end_time = models.DateTimeField(auto_now=True, help_text="ride end time")

    def __str__(self):
        return self.driver_name


class Ride(models.Model):
    """ride model,this has a tree structure using foriegn key.
        """
    user_details = models.ForeignKey('User',  on_delete=models.CASCADE)
    drivers_details = models.ForeignKey('Driver', on_delete=models.CASCADE)
    booking_start_time = models.DateTimeField(auto_now_add=True, help_text="ride start time")
    booking_end_time = models.DateTimeField(auto_now=True, help_text="ride end time")




