from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from datient.managers import DoctorManager

HIERARCHIES = (
    (0, 'Jefe del servicio médico'),
    (1, 'Médico del servicio de clínica médica'),
    (2, 'Médico encargado del internado'),
)

class Doctor(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    hierarchy = models.PositiveSmallIntegerField(choices=HIERARCHIES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = DoctorManager()

    USERNAME_FIELD = 'email'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        if self.hierarchy == 0:
            return True
