from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from ohms_app.models import Doctor

class Command(BaseCommand):
    help = 'Add all doctors to the Doctors group'

    def handle(self, *args, **options):
        doctors = Doctor.objects.all()
        doctors_group = Group.objects.get(name='Doctors')

        for doctor in doctors:
            doctor.user.groups.add(doctors_group)
            doctor.user.save()

        self.stdout.write(self.style.SUCCESS('All doctors added to the group Doctors.'))
