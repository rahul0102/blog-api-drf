from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
)
from rest_framework.mixins import (
    DestroyModelMixin,
    UpdateModelMixin
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from blog.api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = UserCreateSerializer

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data = data)

        if serializer.is_valid(raise_exception = True):
            new_data = data
            return Response(new_data, status = HTTP_200_OK)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
