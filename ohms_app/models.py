from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="Admin")
    specialisation = models.CharField(max_length=255, null=True, blank=True)
    age = models.PositiveBigIntegerField(null=True, blank=True)

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialisation = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        self.first_name = self.user.first_name
        self.last_name = self.user.last_name
        self.role = self.user.role

        super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveBigIntegerField(null=True, blank=True)
    role = models.CharField(max_length=10)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.first_name = self.user.first_name
        self.last_name = self.user.last_name
        self.role = self.user.role

        super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.role} {self.first_name} {self.last_name}"

class HealthMetric(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='metrics')
    pulse = models.IntegerField(null=True, default=80)
    systolic = models.IntegerField(null=True, default=120)
    diastolic = models.IntegerField(null=True, default=80)
    body_temperature = models.FloatField(null=True, default=37)
    steps = models.IntegerField(null=True, default=0)
    calories = models.IntegerField(null=True, default=0)
    date = models.DateField(auto_now_add=True)
