from datetime import date
from datient.models.doctor import Doctor
from datient.models.hospital import Hospitalization
from datient.models.infraestructure import Bed, Room
from datient.models.patient import Patient
import math
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Doctor.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = Doctor
        fields = ('id', 'email', 'hierarchy', 'first_name', 'last_name', 'created_at')

class HospitalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitalization
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = '__all__'

    def get_age(self, obj):
        days = (date.today() - obj.birth_date).days
        return math.floor(days / 365.25)

class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = ('id', 'name', 'room')

class RoomSerializer(serializers.ModelSerializer):
    beds = BedSerializer(many=True, read_only=True, source='bed_set')

    class Meta:
        model = Room
        fields = ('id', 'name', 'beds')

def jwt_response_payload_handler(token, user, request):
    return {
        'token': token,
        'user': DoctorSerializer(user, context={'request': request}).data
    }
