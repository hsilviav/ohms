from django import forms
from .models import HealthMetric

class SensorDataForm(forms.ModelForm):
    class Meta:
        model = HealthMetric
        fields = ['pulse', 'systolic', 'diastolic', 'body_temperature', 'steps', 'calories']
        widgets = {
            'patient': forms.HiddenInput()
        }