from rest_framework import viewsets

from datient.models import ComplementaryStudy, Patient
from datient.serializers import ComplementaryStudySerializer, PatientSerializer


class ComplementaryStudyViewSet(viewsets.ModelViewSet):

    queryset = ComplementaryStudy.objects.all()
    serializer_class = ComplementaryStudySerializer


class PatientViewSet(viewsets.ModelViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        dni = self.request.query_params.get('dni', None)

        if dni is not None:
            queryset = queryset.filter(dni__regex=f'^{dni}')

        return queryset
