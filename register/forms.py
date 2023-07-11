from django import forms
from django.contrib.auth.forms import UserCreationForm
from ohms_app.models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    role = forms.ChoiceField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')])

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email", "role", "password1", "password2"]