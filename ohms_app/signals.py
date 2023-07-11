from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Patient, Doctor

@receiver(post_save, sender=CustomUser)
def create_object(sender, instance, created, **kwargs):
    if created and instance.role == 'doctor':
        Doctor.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, specialisation=instance.specialisation, role=instance.role)
    if created and instance.role == 'patient':
        Patient.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, age=instance.age, role=instance.role)

