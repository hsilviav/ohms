from django.shortcuts import render
from django.http import JsonResponse
import random
from ohms_app.models import Patient, HealthMetric

# Create your views here.

def generate_readings(request):
    pulse = random.randint(45, 110)
    systolic = random.randint(60, 150)
    diastolic = random.randint(30, 90)
    body_temperature = round(random.uniform(35.7, 37.5), 1)
    steps = random.randint(4000, 35000)

    data = {
        'pulse': pulse,
        'systolic': systolic,
        'diastolic': diastolic,
        'body_temperature': body_temperature,
        'steps': steps,
    }

    return JsonResponse(data)

