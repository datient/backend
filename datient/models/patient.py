from django.core.validators import MaxValueValidator
from django.db import models

SEXES = (
    (0, 'Masculino'),
    (1, 'Femenino'),
)

class Patient(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    history_number = models.PositiveIntegerField(blank=True)
    sex = models.PositiveSmallIntegerField(choices=SEXES, validators=[MaxValueValidator(1)])
    income_diagnosis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
