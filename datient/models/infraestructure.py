from datient.models.patient import Patient
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=7)

class Bed(models.Model):
    name = models.CharField(max_length=7)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
