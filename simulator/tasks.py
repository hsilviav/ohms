from simulator.models import Smartwatch
from ohms_app.models import Patient
import random


def perform_mock_readings():
    pulse = random.randint(50, 110)
    systolic = random.randint(100, 140)
    diastolic = random.randint(60, 90)
    body_temperature = round(random.uniform(36.0, 38.5), 1)
    steps = random.randint(1000, 50000)

    patient = Patient.objects.get(id=1)

    smartwatch = Smartwatch.objects.create(
        patient = patient,
        pulse = pulse,
        systolic = systolic,
        diastolic = diastolic,
        body_temperature = body_temperature,
        steps = steps,
    )

    

