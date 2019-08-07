from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from datient.models import Hospitalization
from datient.serializers import HospitalizationSerializer


class HospitalizationViewSet(viewsets.ModelViewSet):

    queryset = Hospitalization.objects.all()
    serializer_class = HospitalizationSerializer

    @action(detail=True, methods=['get'])
    def bed_filter(self, request, pk=None):
        try:
            bed_hospitalization = Hospitalization.objects.filter(bed__id=pk)
            bed_hospitalization = bed_hospitalization.order_by('-done_at')[0]
            dni = bed_hospitalization.patient.dni
        except IndexError:
            raise NotFound({
                    'detail': 'No se han encontrado hospitalizaciones'
                })

        dni_hospitalization = Hospitalization.objects.filter(patient__dni=dni)
        dni_hospitalization = dni_hospitalization.order_by('-done_at')[0]

        if (bed_hospitalization.id == dni_hospitalization.id and
            dni_hospitalization.left_at is None):
            serializer = self.get_serializer(dni_hospitalization, many=False)
            return Response(serializer.data)

        raise NotFound({'detail': 'No se han encontrado hospitalizaciones'})

    @action(detail=True, methods=['get'])
    def patient_filter(self, request, pk=None):
        try:
            dni_hospitalization = Hospitalization.objects.filter(patient__dni=pk)
            dni_hospitalization = dni_hospitalization.order_by('-done_at')[0]
            bedId = dni_hospitalization.bed.id
        except IndexError:
            raise NotFound({
                    'detail': 'No se han encontrado hospitalizaciones'
                })

        bed_hospitalization = Hospitalization.objects.filter(bed__id=bedId)
        bed_hospitalization = bed_hospitalization.order_by('-done_at')[0]

        if (dni_hospitalization.id == bed_hospitalization.id and
            bed_hospitalization is None):
            serializer = self.get_serializer(bed_hospitalization, many=False)
            return Response(serializer.data)

        raise NotFound({'detail': 'No se han encontrado hospitalizaciones'})
