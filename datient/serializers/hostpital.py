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
