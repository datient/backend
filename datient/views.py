from datient.models.doctor import Doctor
from datient.models.hospital import Hospitalization
from datient.models.infraestructure import Bed, Room
from datient.models.patient import Patient, ComplementaryStudy
from datient.serializers import *
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_jwt.views import JSONWebTokenAPIView

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class HospitalizationViewSet(viewsets.ModelViewSet):
    queryset = Hospitalization.objects.all()
    serializer_class = HospitalizationSerializer

class ComplementaryStudyViewSet(viewsets.ModelViewSet):
    queryset = ComplementaryStudy.objects.all()
    serializer_class = ComplementaryStudySerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ObtainJSONWebToken(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer

obtain_jwt_token = ObtainJSONWebToken.as_view()
