from django.urls import path

from . import views
from .views import *

from rest_framework import routers


urlpatterns = [

    path('user/', api_user_details_update, name='user_update'),
    path('driver/', api_driver_details_update, name='driver_update'),
    path('ride/', api_ride_details_update, name='ride_update'),


]