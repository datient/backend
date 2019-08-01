from rest_framework import serializers

from . import HospitalizationSerializer
from datient.models import Bed, Room


class BedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bed
        fields = ('id', 'name', 'room')


class RoomSerializer(serializers.ModelSerializer):

    beds = BedSerializer(many=True, read_only=True, source='bed_set')

    class Meta:
        model = Room
        fields = ('id', 'name', 'beds')
