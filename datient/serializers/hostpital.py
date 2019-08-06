from django.utils.timezone import now
from rest_framework import serializers

from . import ProgressSerializer
from datient.models import Hospitalization, Progress


class HospitalizationSerializer(serializers.ModelSerializer):

    boarding_days = serializers.SerializerMethodField()
    progress = ProgressSerializer()

    class Meta:
        model = Hospitalization
        fields = ('id', 'entry_at', 'left_at', 'done_at',
                  'bed', 'doctor', 'patient', 'boarding_days',
                  'progress')

    def create(self, validated_data):
        progress_data = validated_data.pop('progress')
        progress = Progress.objects.create(**progress_data)
        hospitalization = Hospitalization.objects.create(progress=progress,
                                                         **validated_data)
        return hospitalization

    def get_boarding_days(self, obj):
        if obj.entry_at is not None:
            return (now() - obj.entry_at).days
        
        return None
