from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from .router import router
from .views import generate_pdf, obtain_jwt_token

static_media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', obtain_jwt_token),
    path('accounts/', include('rest_registration.api.urls')),
    path('pdf/<int:dni>', generate_pdf),
] + static_media
