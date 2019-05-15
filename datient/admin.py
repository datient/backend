from django.contrib import admin
from datient.models.doctor import Doctor
from datient.models.patient import Patient

def full_name(obj):
    return f'{obj.first_name} {obj.last_name}'

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('email', full_name, 'hierarchy')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient)
