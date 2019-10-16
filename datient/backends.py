from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password

from datient.models import Doctor


class SettingsBackend(ModelBackend):

    def authenticate(self, request=None, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(Doctor.USERNAME_FIELD)
        try:
            user = Doctor.objects.get(email=username)
        except Doctor.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
