from rest_framework import serializers
from .models import User, Driver, Ride


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'mobile_number', 'booking_start_time', 'booking_end_time')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'driver_name', 'mobile_number', 'booking_start_time', 'booking_end_time')


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('id', 'ride_status', 'user_details', 'driver_details', 'booking_start_time', 'booking_end_time')
