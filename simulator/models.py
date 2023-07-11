from django.db import models
from ohms_app.models import Patient

# Create your models here.

class Smartwatch(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    pulse = models.IntegerField()
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    body_temperature = models.FloatField()
    steps = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Smartwatch Data for {self.patient}"