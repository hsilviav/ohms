from django.test import TestCase
from .models import CustomUser, Doctor, Patient, HealthMetric
from simulator.models import Smartwatch


class OhmsAppTests(TestCase):
    def test_setUp(self):
        #create a user
        user = CustomUser.objects.create(username="testuser", email="test@example.com")

        #cerate a doctor
        doctor = Doctor.objects.create(user=user, specialisation='Cardiology')

        #create a patient
        patient = Patient.objects.create(user=user, doctor=doctor, first_name='John', last_name='Doe')

        self.assertEqual(patient.doctor, doctor)

        health_metrics = HealthMetric.objects.create(
        patient=patient, pulse=80, systolic=110, diastolic=69, body_temperature=36.5)

        smartwatch = Smartwatch.objects.create(
        patient=patient, pulse=80, systolic=110, diastolic=69, body_temperature=36.5, steps=8000)

        self.assertEqual(health_metrics.patient, patient)
        self.assertEqual(health_metrics.pulse, 80)
        self.assertEqual(health_metrics.systolic, 110)
        self.assertEqual(health_metrics.diastolic, 69)
        self.assertEqual(health_metrics.body_temperature, 36.5)

        self.assertEqual(smartwatch.patient, patient)
        self.assertEqual(smartwatch.pulse, 80)
        self.assertEqual(smartwatch.systolic, 110)
        self.assertEqual(smartwatch.diastolic, 69)
        self.assertEqual(smartwatch.body_temperature, 36.5)
        self.assertEqual(smartwatch.steps, 8000)



