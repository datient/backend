from django.test import TestCase

# Create your tests here.

from datient.models import Doctor, Hospitalization, Bed, Room, Patient

from rest_framework.test import APIRequestFactory

class DoctorTestCase(TestCase):
    def setUp(self):
        Doctor.objects.create(first_name="Tomas", last_name="Ledesma",
                              email="totem.ledesma@gmail.com", hierarchy=0)
        Doctor.objects.create(first_name="Ivan", last_name="Nunies",
                              email="ivanluis.cba@gmail.com", hierarchy=1)
        Doctor.objects.create(first_name="Oliver", last_name="Oliver",
                              email="facu191019@gmail.com", hierarchy=2)
        

#    def test_animals_can_speak(self):
#        """Animals that can speak are correctly identified"""
#        lion = Animal.objects.get(name="lion")
#        cat = Animal.objects.get(name="cat")
#        self.assertEqual(lion.speak(), 'The lion says "roar"')
#        self.assertEqual(cat.speak(), 'The cat says "meow"')

class RoomTestCase(TestCase):
    def setUp(self):
        Room.objects.create(name="Tetris")

class BedTestCase(TestCase):
    def setUp(self):
        Bed.objects.create(name="Cube")

class PatientTestCase(TestCase):
    def setUp(self):
        Patient.objects.create(first_name="Tincho", last_name="Olivari")

#----------------------------------------------------------
# Doctor.objects.create(first_name="Oliver", last_name="Mills",
                    #   email="oliver@gmail.com", hierarchy=0)

factory = APIRequestFactory()

request = factory.post('http://localhost:8000/api/hospitalization/', {'doctor': 'Oliver'} )
