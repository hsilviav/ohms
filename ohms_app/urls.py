from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('patients/input/', views.patient_input, name="input"),
    path('patients/view/', views.patient_view, name="view"),
    path('doctors/view_patients/', views.doctors_view, name="view_patients"),
    path('doctors/view_data/<str:first_name>/<str:last_name>/', views.doctors_data, name="view_data"),
    path('profile/', views.profile, name="profile"),

]