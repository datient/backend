from datetime import date
import math

from rest_framework import serializers

from datient.models import ComplementaryStudy, Patient, Progress


class ComplementaryStudySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComplementaryStudy
        fields = '__all__'


class ProgressSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Progress
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
  
    age = serializers.SerializerMethodField()
    studies = ComplementaryStudySerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

    def get_age(self, obj):
        days = (date.today() - obj.birth_date).days + 1
        return math.floor(days / 365.25)
