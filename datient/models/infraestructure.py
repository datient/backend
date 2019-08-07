from django.db import models

from datient.models.patient import Patient


class Room(models.Model):

    name = models.CharField(max_length=7)

    def __str__(self):
        return f'{self.name}'


class Bed(models.Model):

    name = models.CharField(max_length=12)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
