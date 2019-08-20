from django.db import models

from datient.models.doctor import Doctor
from datient.models.infraestructure import Bed
from datient.models.patient import Patient, Progress


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
