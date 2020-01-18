from django.shortcuts import render


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *




@api_view(['GET', 'POST'])
def api_user_details_update(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_driver_details_update(request):
    if request.method == 'GET':
        user = Driver.objects.all()
        serializer = DriverSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_ride_details_update(request):
    if request.method == 'GET':
        user = Ride.objects.all()
        serializer = RideSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)