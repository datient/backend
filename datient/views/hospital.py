from rest_framework import viewsets

from datient.models import Hospitalization
from datient.serializers import HospitalizationSerializer


class HospitalizationViewSet(viewsets.ModelViewSet):

    queryset = Hospitalization.objects.all()
    serializer_class = HospitalizationSerializer
