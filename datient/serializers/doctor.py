from rest_framework import serializers

from datient.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = ('id', 'email', 'hierarchy', 'first_name', 
                  'last_name', 'created_at')
