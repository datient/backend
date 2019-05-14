from datient.views import DoctorViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
