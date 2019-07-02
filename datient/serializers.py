from datetime import date
from datient.models.doctor import Doctor
from datient.models.hospital import Hospitalization
from datient.models.infraestructure import Bed, Room
from datient.models.patient import Patient, ComplementaryStudy, Progress
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
import math

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

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

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'

class HospitalizationSerializer(serializers.ModelSerializer):
    progress = ProgressSerializer()

    class Meta:
        model = Hospitalization
        fields = ('id', 'entry_at', 'left_at', 'done_at', 'bed', 'doctor', 'patient', 'progress')

class ComplementaryStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplementaryStudy
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    studies = ComplementaryStudySerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

    def get_age(self, obj):
        days = (date.today() - obj.birth_date).days
        return math.floor(days / 365.25)

class BedSerializer(serializers.ModelSerializer):
    hospitalizations = HospitalizationSerializer(many=True, read_only=True)

    class Meta:
        model = Bed
        fields = ('id', 'name', 'room', 'hospitalizations')

class RoomSerializer(serializers.ModelSerializer):
    beds = BedSerializer(many=True, read_only=True, source='bed_set')

    class Meta:
        model = Room
        fields = ('id', 'name', 'beds')

class JSONWebTokenSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = 'Email y/o contraseña incorrecta'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "{username_field}" and "password".'
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)    

def jwt_response_payload_handler(token, user, request):
    return {
        'token': token,
        'user': DoctorSerializer(user, context={'request': request}).data
    }
