from rest_framework import serializers

from . import ProgressSerializer
from datient.models import Hospitalization


class HospitalizationSerializer(serializers.ModelSerializer):

    progress = ProgressSerializer()

    class Meta:
        model = Hospitalization
        fields = ('id', 'entry_at', 'left_at', 'done_at',
                  'bed', 'doctor', 'patient', 'progress')
