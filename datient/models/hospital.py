from django.db import models
from django.utils.timezone import now

from datient.models import Bed, Doctor, Patient


class Hospitalization(models.Model):

    entry_at = models.DateTimeField(blank=True, null=True)
    left_at = models.DateTimeField(blank=True, null=True)
    done_at = models.DateTimeField(auto_now=True)
    bed = models.ForeignKey(Bed, related_name='hospitalizations',
                            on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor}: {self.patient} - {self.done_at}'

    @property
    def boarding_days(self):
        if self.entry_at is not None:
            return (now() - self.entry_at).days
        return None

    def save(self, *args, **kwargs):
        dni = self.patient
        hosp = Hospitalization.objects.filter(patient__dni=str(dni)).last()
        if (hosp is None or hosp.left_at is not None):
            self.entry_at = now()
        elif (hosp.left_at is None):
            self.entry_at = hosp.entry_at
        super().save(*args, **kwargs)
