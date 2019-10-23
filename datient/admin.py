from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from datient.models import (Bed, Doctor, ComplementaryStudy, FuturePlan,
                            Hospitalization, Patient, Progress, Room)


@admin.register(Doctor)
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


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')


class BedInLine(admin.TabularInline):

    model = Bed


@admin.register(ComplementaryStudy)
class ComplementaryStudyAdmin(admin.ModelAdmin):

    list_display = ('id', 'image', 'patient')


@admin.register(FuturePlan)
class FuturePlanAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'description', 'patient')


@admin.register(Hospitalization)
class HospitalizationAdmin(admin.ModelAdmin):

    list_display = ('id', 'doctor', 'patient', 'bed', 'entry_at', 'done_at')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = ('dni', 'full_name', 'age', 'gender')
    list_filter = ('gender',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = [BedInLine]
    ordering = ('pk',)


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):

    list_display = ('id', 'diagnosis', 'status', 'patient')
    list_filter = ('status',)


admin.site.unregister(Group)
