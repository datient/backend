from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from datient.models.doctor import Doctor
from datient.models.hospital import Hospitalization
from datient.models.infraestructure import Bed, Room
from datient.models.patient import (Patient, ComplementaryStudy,
                                    Progress, FuturePlan)


class DoctorAdmin(UserAdmin):

    list_display = ('email', 'full_name', 'hierarchy')
    list_filter = ('is_active', 'hierarchy')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('hierarchy', 'is_active')})
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('hierarchy', 'is_active')})
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class BedInLine(admin.TabularInline):

    model = Bed


class RoomAdmin(admin.ModelAdmin):

    inlines = [BedInLine]
    ordering = ('pk',)


class HospitalizationAdmin(admin.ModelAdmin):

    list_display = ('doctor', 'patient', 'bed', 'done_at')


admin.site.register(Bed)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Hospitalization, HospitalizationAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Patient)
admin.site.register(ComplementaryStudy)
admin.site.register(Progress)
admin.site.register(FuturePlan)
admin.site.unregister(Group)
