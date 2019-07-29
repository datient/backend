from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from datient.models import Hospitalization
from datient.serializers import HospitalizationSerializer


class HospitalizationViewSet(viewsets.ModelViewSet):

    queryset = Hospitalization.objects.all()
    serializer_class = HospitalizationSerializer

    @action(detail=True, methods=['get'])
    def bed_filter(self, request, pk=None):
        queryset = Hospitalization.objects.filter(bed__id=pk)
        try:
            queryset = queryset.order_by('-done_at')[0]
        except IndexError:
            return Response({'status': 'No se han encontrado hospitalizaciones'})

        dni = queryset.patient.dni

        segunda = Hospitalization.objects.filter(patient__dni=dni)
        segunda = segunda.order_by('-done_at')[0]

        serializer = self.get_serializer(segunda, many=False)

        if (queryset.id == segunda.id):
            return Response(serializer.data)

        return Response({'status': 'No se han encontrado hospitalizaciones'})
