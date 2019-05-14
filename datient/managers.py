from django.contrib.auth.models import BaseUserManager

class DoctorManager(BaseUserManager):
    def create_user(self, email, password, **validated_data):
        if not email:
            raise ValueError('Doctors must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            **validated_data,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.hierarchy = 0
        user.save()
        return user
