from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from ohms_app.models import Patient

class Command(BaseCommand):
    help = 'Add all patients to the Patients group'

    def handle(self, *args, **options):
        patients = Patient.objects.all()
        patients_group = Group.objects.get(name='Patients')

        for patient in patients:
            patient.user.groups.add(patients_group)
            patient.user.save()

        self.stdout.write(self.style.SUCCESS('All patients added to the group Patients.'))
