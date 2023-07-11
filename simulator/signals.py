from django.db.models.signals import post_save
from django.dispatch import receiver
from ohms_app.models import HealthMetric
from simulator.models import Smartwatch

@receiver(post_save, sender=Smartwatch)
def create_health_metric(sender, instance, created, **kwargs):
    if created: 
        HealthMetric.objects.create(
            patient = instance.patient,
            pulse = instance.pulse,
            systolic = instance.systolic,
            diastolic = instance.diastolic,
            body_temperature = instance.body_temperature,
            steps = instance.steps,
        )