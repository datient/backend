from django.utils.timezone import now
from rest_framework import serializers

from . import ProgressSerializer
from datient.models import Hospitalization, Progress


class HospitalizationSerializer(serializers.ModelSerializer):

    boarding_days = serializers.SerializerMethodField()

    class Meta:
        model = Hospitalization
        fields = ('id', 'entry_at', 'left_at', 'done_at',
                  'bed', 'doctor', 'patient', 'boarding_days')

    def get_boarding_days(self, obj):
        if obj.entry_at is not None:
            return (now() - obj.entry_at).days
        
        return None

    def create(self, validated_data):
        dni = validated_data['patient']
        hospitalization = Hospitalization.objects.filter(patient__dni=str(dni)).last()
        if (hospitalization is None):
            validated_data['entry_at'] = now()
            return Hospitalization.objects.create(**validated_data)
        if (hospitalization.left_at is not None):
            validated_data['entry_at'] = now()
            return Hospitalization.objects.create(**validated_data)
        if (hospitalization.left_at is None):
            validated_data['entry_at'] = hospitalization.entry_at
            return Hospitalization.objects.create(**validated_data)
