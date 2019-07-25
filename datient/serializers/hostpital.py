from rest_framework import serializers

from . import ProgressSerializer
from datient.models import Hospitalization, Progress


class HospitalizationSerializer(serializers.ModelSerializer):

    progress = ProgressSerializer()

    class Meta:
        model = Hospitalization
        fields = ('id', 'entry_at', 'left_at', 'done_at',
                  'bed', 'doctor', 'patient', 'progress')

    def create(self, validated_data):
        progress_data = validated_data.pop('progress')
        progress = Progress.objects.create(**progress_data)
        hospitalization = Hospitalization.objects.create(progress=progress,
                                                         **validated_data)
        return hospitalization
