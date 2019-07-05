from rest_framework import routers

from datient.views import (BedViewSet, ComplementaryStudyViewSet,
                           DoctorViewSet, HospitalizationViewSet,
                           PatientViewSet, RoomViewSet)

router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet)
router.register(r'room', RoomViewSet)
router.register(r'bed', BedViewSet)
router.register(r'patient', PatientViewSet)
router.register(r'hospitalization', HospitalizationViewSet)
router.register(r'study', ComplementaryStudyViewSet)
