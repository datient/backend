from rest_framework import viewsets

from datient.models import Doctor
from datient.serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
