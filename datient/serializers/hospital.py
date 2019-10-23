from rest_framework import serializers

from datient.models import Hospitalization


class HospitalizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospitalization
        fields = ('id', 'entry_at', 'left_at', 'done_at',
                  'bed', 'doctor', 'patient', 'boarding_days')
