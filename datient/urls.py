from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from .router import router
from .views import activate, generate_pdf, generate_statistics, obtain_jwt_token

static_media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', obtain_jwt_token),
    path('accounts/', include('rest_registration.api.urls')),
    path('pdf/<int:dni>', generate_pdf),
    path('statistics/', generate_statistics),
    path('activate/<slug:uidb64>/<slug:token>', activate),
] + static_media
