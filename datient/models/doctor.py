from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from datient.managers import DoctorManager
from datient.tokens import account_activation_token

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
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = DoctorManager()

    USERNAME_FIELD = 'email'

    def capitalize_names(self):
        names = [name.capitalize() for name in self.first_name.split()]
        self.first_name = ' '.join(names)
        last_names = [ln.capitalize() for ln in self.last_name.split()]
        self.last_name = ' '.join(last_names)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

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

    def save(self, *args, **kwargs):
        self.capitalize_names()
        super().save(*args, **kwargs)
        if not self.is_active:
            subject = f'Activar cuenta: {self.email}'
            message = render_to_string('email/email.html', {
                'user': self,
                'domain': 'http://localhost:8000/activate',
                'uid': urlsafe_base64_encode(force_bytes(self.pk)),
                'token': account_activation_token.make_token(self),
            })
            from_email = settings.EMAIL_HOST
            recipient_list = ['teamdatient@gmail.com',]
            send_mail(
                subject,
                '',
                from_email,
                recipient_list,
                fail_silently=False,
                html_message=message
            )
