from rest_framework_jwt import views

from datient.serializers import JSONWebTokenSerializer


class ObtainJSONWebToken(views.JSONWebTokenAPIView):

    serializer_class = JSONWebTokenSerializer


obtain_jwt_token = ObtainJSONWebToken.as_view()
