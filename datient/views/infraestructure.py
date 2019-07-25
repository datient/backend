from rest_framework import viewsets

from datient.models import Bed, Room
from datient.serializers import BedSerializer, RoomSerializer


class BedViewSet(viewsets.ModelViewSet):

    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class RoomViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
