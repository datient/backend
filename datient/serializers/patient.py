from datetime import date
import math

from rest_framework import serializers

from datient.models import (ComplementaryStudy, FuturePlan, Patient, Progress)


class ComplementaryStudySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComplementaryStudy
        fields = '__all__'


class FuturePlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = FuturePlan
        fields = '__all__'


class ProgressSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Progress
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
  
    age = serializers.SerializerMethodField()
    plans = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    studies = ComplementaryStudySerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

    def get_age(self, obj):
        return obj.age

    def get_progress(self, obj):
        progress = obj.progress.all().order_by('-created_at')
        return ProgressSerializer(progress, many=True, read_only=True).data

    def get_plans(self, obj):
        plans = obj.plans.all().order_by('-created_at')
        return FuturePlanSerializer(plans, many=True, read_only=True).data
