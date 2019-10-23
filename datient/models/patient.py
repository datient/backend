from datetime import date
import math

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

GENDERS = (
    (0, 'Masculino'),
    (1, 'Femenino'),
)


class Patient(models.Model):

    dni = models.PositiveIntegerField(primary_key=True, unique=True,
        validators=[
            MinValueValidator(1000000),
            MaxValueValidator(99999999)
        ]
    )
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    birth_date = models.DateField()
    history_number = models.PositiveIntegerField(blank=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDERS,
                                              validators=[MaxValueValidator(1)])
    contact = models.CharField(max_length=16, blank=True, null=True)
    contact2 = models.CharField(max_length=16, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.dni}'

    @property
    def age(self):
        days = (date.today() - self.birth_date).days + 1
        return math.floor(days / 365.25)

    @property
    def get_gender(self):
        return 'Masculino' if self.gender == 0 else 'Femenino'

    @property
    def full_name(self):
        return f'{self.last_name}, {self.first_name}'

    def save(self, *args, **kwargs):
        names = [name.capitalize() for name in self.first_name.split()]
        self.first_name = ' '.join(names)
        last_names = [ln.capitalize() for ln in self.last_name.split()]
        self.last_name = ' '.join(last_names)
        super().save(*args, **kwargs)


STATUS = (
    (0, 'Bien'),
    (1, 'Precaucion'),
    (2, 'Peligro'),
)


class ComplementaryStudy(models.Model):

    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                                related_name='studies')

    class Meta:
        verbose_name_plural = 'Complementary Studies'

    def __str__(self):
        return f'{self.patient}: {self.image}'


class FuturePlan(models.Model):

    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                                related_name='plans')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.title}'


class Progress(models.Model):

    diagnosis = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS)
    has_left = models.BooleanField(default=False)
    income = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                                related_name='progress')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Progress'

    def __str__(self):
        return f'{self.id}'
