from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from accounts.api.permissions import IsNotAuthenticated
from accounts.api.v1.serializers.login import LoginSerializer
from accounts.services.login import LoginService


class LoginView(GenericAPIView):

    permission_classes = [IsNotAuthenticated]
    serializer_class = LoginSerializer

    @swagger_auto_schema(responses={status.HTTP_204_NO_CONTENT: openapi.Response("")})
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        response = LoginService.login(request, user)
        return response


class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={status.HTTP_204_NO_CONTENT: openapi.Response("")})
    def post(self, request):
        response = LoginService.logout(request)
        return response
