from datient.views import *
from datient.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet)
router.register(r'hospitalization', HospitalizationViewSet)
router.register(r'patient', PatientViewSet)
router.register(r'room', RoomViewSet)
router.register(r'bed', BedViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', obtain_jwt_token),
    path('accounts/', include('rest_registration.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
