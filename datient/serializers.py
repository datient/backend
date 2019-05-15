from datient.models.doctor import Doctor
from datient.models.patient import Patient
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
        fields = ('id', 'email', 'password', 'hierarchy', 'first_name', 'last_name', 'created_at')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

def jwt_response_payload_handler(token, user, request):
    return {
        'token': token,
        'user': DoctorSerializer(user, context={'request': request}).data
    }
