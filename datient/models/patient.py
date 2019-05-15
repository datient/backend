from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

GENDERS = (
    (0, 'Masculino'),
    (1, 'Femenino'),
)

class Patient(models.Model):
    dni = models.PositiveIntegerField(primary_key=True, unique=True,
        validators=[
            MinValueValidator(10000000),
            MaxValueValidator(99999999)
        ]
    )
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    birth_date = models.DateField()
    history_number = models.PositiveIntegerField(blank=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDERS, validators=[MaxValueValidator(1)])
    income_diagnosis = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.dni}'
