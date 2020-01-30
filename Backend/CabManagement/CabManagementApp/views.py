from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ViewSet):
    """
    Listing all the users
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    """
    To retrieve a particular user
    """

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    """
    To create a new user
    """
    def create(self, request):
        serializer = User(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED )


class DriverViewSet(viewsets.ViewSet):
    """
    Listing all the drivers
    """
    def list(self, request):
        queryset = Driver.objects.all()
        serializer = DriverSerializer(queryset, many=True)
        return Response(serializer.data)

    """
    To retrieve a particular driver
    """

    def retrieve(self, request, pk=None):
        queryset = Driver.objects.all()
        driver = get_object_or_404(queryset, pk=pk)
        serializer = DriverSerializer(driver)
        return Response(serializer.data)

    """
    To create a new driver
    """
    def create(self, request):
        serializer = DriverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RideViewSet(viewsets.ViewSet):
    """
    Listing all the ride lists
    """
    def list(self, request):
        queryset = Ride.objects.all()
        user = request.GET.get('user', None)
        driver = request.GET.get('driver', None)
        status = request.GET.get('status', None)
        if user is not None:
            queryset = queryset.filter(user__username=user)
        if driver is not None:
            queryset = queryset.filter(driver__drivername=driver)
        if status is not None:
            queryset = queryset.filter(status=status)
        serializer = RideSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print("This is Create start", request.data)
        try:
            user = User.objects.get(id=request.data['user'])
            print("Try block", user)
        except User.DoesNotExist:
            print("Except block")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        requested = Ride.objects.filter(user=user).filter(status='RE').count()
        accepted = Ride.objects.filter(user=user).filter(status='AC').count()
        # print("Queryset", len(queryset))
        if requested > 0:
            return Response("Already Requested", status=status.HTTP_226_IM_USED)
        if accepted > 0:
            return Response("Ride is ongoing", status=status.HTTP_403_FORBIDDEN)
        serializer = RideCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        ride = Ride.objects.get(id=pk)
        status = request.data.get('status', None)
        if status == 'accept' or status == 'done':
            ride.status = status
        if status == 'AC':
            driver_name = request.data.get('driver', None)
            if driver_name is not None:
                try:
                    driver = Driver.objects.get(drivername=driver_name)
                    ride.driver = driver
                except Driver.DoesNotExist:
                    return Response("Driver doesnot exist", status=status.HTTP_400_BAD_REQUEST)
        ride.save()

