from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        tags=["authentication"],
        operation_summary="Register user",
        request_body=UserSerializer(),
        responses={
            status.HTTP_201_CREATED: UserSerializer(),
            status.HTTP_400_BAD_REQUEST: "Invalid data",
        },
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        data = self.request.data
        user = User(username=data["username"], email=data["email"])
        user.set_password(data["password"])
        user.save()
        serializer.instance = user
        serializer.save()
