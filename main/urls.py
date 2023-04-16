from django.urls import path
from .views import *

urlpatterns = [
    path("",home ,name="home"),
    path("predict",predicted_car,name="predict_car"),
]