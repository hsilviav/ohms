from typing import Any, Dict, List, Optional, Tuple
from django.contrib import admin
from django.http.request import HttpRequest
from .models import CustomUser, Doctor, Patient, HealthMetric

# Register your models here.

class RoleDisplay(admin.ModelAdmin):
    list_display = ['role']

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialisation')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'doctor')

class HealthMetricAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(HealthMetric, HealthMetricAdmin)
