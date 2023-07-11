from django.test import TestCase
from .models import CustomUser, Doctor, Patient, HealthMetric

# Create your tests here.

# class CustomUserModelTestCase(TestCase):
#     def test_customuser_creation(self):
#         user = CustomUser.objects.create_user(
#             username = "testuser",
#             email = "test@example.com",
#             password = "testpassword",
#             role = "doctor",
#             specialisation = "Cardiology",
#             age = 30
#         )

#         self.assertEqual(user.username, "testuser")
#         self.assertEqual(user.email, "test@example.com")
#         self.assertEqual(user.password, "testpassword")
#         self.assertEqual(user.specialisation, "Cardiology")
#         self.assertEqual(user.age, "30")
