from django.shortcuts import render, get_object_or_404
from .forms import SensorDataForm
from .models import Doctor, Patient, HealthMetric
from .utils import isInRange

# Create your views here.

def home(response):
    return render(response, "ohms_app/home.html", {})

def profile(request):
    user = request.user
    role = user.role

    if role == 'patient':
        patient = Patient.objects.get(user=user)
        age = patient.age
        assigned_doctor = patient.doctor
        context = {'user': user, 'age': age, 'assigned_doctor': assigned_doctor}
    elif role == 'doctor':
        doctor = Doctor.objects.get(user=user)
        specialisation = doctor.specialisation
        context = {'user': user, 'specialisation': specialisation}
    else:
        context = {'user': user}

    return render(request, "ohms_app/profile.html", context)

def patient_view(request):
   
    patient = Patient.objects.get(user=request.user)
    health_metrics = HealthMetric.objects.filter(patient=patient)

    for m in health_metrics:
        m.pulse_in_range = isInRange(m.pulse, 60, 100)
        m.systolic_in_range = isInRange(m.systolic, 60, 120)
        m.diastolic_in_range = isInRange(m.diastolic, 40, 80)
        m.body_in_range = isInRange(m.body_temperature, 36.1, 37.2)
        m.steps_in_range = isInRange(m.steps, 7500, 25000)
        m.calories_in_range = isInRange(m.calories, 1750, 2700)

        
    return render(request, "ohms_app/patients/view.html", {'health_metrics': health_metrics})

def patient_input(request):
    if request.method == 'POST':
        form = SensorDataForm(request.POST)
        if form.is_valid():
            health_metric = form.save(commit=False)
            patient = Patient.objects.get(user=request.user)
            health_metric.patient = patient
            health_metric.save()
            success = True
            return render(request, "ohms_app/home.html", {'success': success})
    else:
        patient = Patient.objects.get(user=request.user)
        form = SensorDataForm(initial={'patient': patient})
    return render(request, "ohms_app/patients/input.html", {'form':form})

def doctors_view(request):
    doctor = Doctor.objects.get(user=request.user)
    patients = Patient.objects.filter(doctor=doctor)
    return render(request, "ohms_app/doctors/view_patients.html", {'patients': patients})

def doctors_data(request, first_name, last_name):
    
    patient = get_object_or_404(Patient, first_name=first_name, last_name=last_name)
    health_metrics = HealthMetric.objects.filter(patient=patient)
    
    for m in health_metrics:
        m.pulse_in_range = isInRange(m.pulse, 60, 100)
        m.systolic_in_range = isInRange(m.systolic, 60, 120)
        m.diastolic_in_range = isInRange(m.diastolic, 40, 80)
        m.body_in_range = isInRange(m.body_temperature, 36.1, 37.2)
        m.steps_in_range = isInRange(m.steps, 7500, 25000)
        m.calories_in_range = isInRange(m.calories, 1750, 2700)

    return render(request, "ohms_app/doctors/view_data.html", {'patient': patient, 'health_metrics': health_metrics})
