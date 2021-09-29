from django.urls import path
from .views import *

urlpatterns = [
    path('get-all/',get_all,name="get-all"),
    path('get-all/house/<str:house_name>/',get_all_house,name="get-all"),
    path('get-all/bus/<str:bus_name>/',get_all_bus,name="get-all"),
    path('get-one-detail/<str:Name>/',get_one,name="get-all"),
]
