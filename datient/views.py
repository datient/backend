from datient.models.doctor import Doctor
from datient.models.patient import Patient
from datient.serializers import DoctorSerializer, PatientSerializer
from django.shortcuts import render
from rest_framework import viewsets

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
