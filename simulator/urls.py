from django.urls import path
from .views import generate_readings

urlpatterns = [
    path('readings/', generate_readings, name='generate_readings'),

]