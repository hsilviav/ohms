from django.contrib import admin
from .models import Smartwatch

# Register your models here.

class SmartwatchAdmin(admin.ModelAdmin):
     list_display = ['patient', 'recorded_at']

admin.site.register(Smartwatch, SmartwatchAdmin)
