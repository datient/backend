from rest_framework import serializers

from datient.models import Bed, Hospitalization, Room


class BedSerializer(serializers.ModelSerializer):

    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Bed
        fields = ('id', 'name', 'room', 'is_available')

    def get_is_available(self, obj):
        try:
            hosp = Hospitalization.objects.filter(bed__id=obj.id).order_by('done_at').last()
            dni = hosp.patient.dni
            hosp2 = Hospitalization.objects.filter(patient__dni=dni).order_by('done_at').last()
            if (hosp.id == hosp2.id and hosp2.left_at is None):
                return False
            return True
        except:
            return True


class RoomSerializer(serializers.ModelSerializer):

    beds = BedSerializer(many=True, read_only=True, source='bed_set')

    class Meta:
        model = Room
        fields = ('id', 'name', 'beds')
