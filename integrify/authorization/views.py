from django.contrib.auth.models import User

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .serializers import RegisterSerializer, UserLoginSerializer

from rest_framework import generics, status
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)
   
    def put(self, request, key, format=None):
        user = request.user
        if request.data['password1'] != request.data['password2']:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'password1': "password fields dont match !"}
            )

        if not user.check_password(request.data['old_password']):
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data={"old_password": "old password is not correct !"}
            )

        if user.profile.key != key:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={"authorize": "You dont have permission for this user !"}
            )

        try:
            validate_password(request.data['password1'], user=user)
        except ValidationError as ex:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"detail": {"password": ex}}
            )

        instance = User.objects.get(profile__key=key)
        instance.set_password(request.data['password1'])
        instance.save()
        return Response(
            status=status.HTTP_200_OK, data={"detail": "password changed"}
        )

class UserLoginView(TokenViewBase):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                status=status.HTTP_205_RESET_CONTENT,
                data={'detail': "logged out"}
            )

        except Exception:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"detail": "refresh_token is not valid"}
            )


