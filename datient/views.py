from datient.models.doctor import Doctor
from datient.serializers import DoctorSerializer
from django.shortcuts import render
from rest_framework import viewsets

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
