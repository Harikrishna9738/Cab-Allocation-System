from rest_framework import serializers
from .models import User, Driver, Ride


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', )

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'driver_name', )


class RideSerializer(serializers.ModelSerializer):
    user_details = UserSerializer()
    driver_details = DriverSerializer()

    class Meta:
        model = Ride
        fields = ('id', 'ride_status', 'user_details', 'driver_details', 'booking_start_time')


class RideCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ("user_name", "ride_status",)


class RideUpdateSerializer(serializers.ModelSerializer):
    driver = Driver()

    class Meta:
        model = Ride
        fields = ("driver_name", "ride_status",)
