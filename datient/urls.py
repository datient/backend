from datient.views import DoctorViewSet
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', obtain_jwt_token),
]
