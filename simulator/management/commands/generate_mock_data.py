# import random
# from datetime import datetime
# from simulator.models import Smartwatch
# from ohms_app.models import Patient, HealthMetric
# from django.core.management.base import BaseCommand

# class Command(BaseCommand):
#     help = 'Generates mock data fro the simulator app'

#     def handle(self, *args, **options):
#         patients = Patient.objects.all()
#         for p in patients:
#             pulse = random.randint(60, 100)
#             systolic = random.randint(90, 140)
#             diastolic = random.randint(60, 90)
#             body_temperature = round(random.uniform(36.0, 38.5), 1)
#             #steps = random.randint(1000, 50000)
#             recorded_at = datetime.now()

#             smartwatch_data = Smartwatch.objects.create(patient=p, pulse=pulse, systolic=systolic, diastolic=diastolic, body_temperature=body_temperature, recorded_at=recorded_at)
#             HealthMetric.objects.create(patient=p, pulse=pulse, systolic=systolic, diastolic=diastolic, body_temperature=body_temperature, date=recorded_at)

#         self.stdout.write(self.style.SUCCESS('Mock data generated!'))

