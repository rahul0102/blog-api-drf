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
    UserDetailsSerializer
)
from rest_framework.mixins import (
    DestroyModelMixin,
    UpdateModelMixin
)

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.decorators import detail_route, list_route

from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from blog.api.permissions import IsOwnerOrReadOnly, IsAdminOrAccountOwner
from django.contrib.auth.models import User


class UserViewSet(ModelViewSet):

    """
    login:
        Login a user.

    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """

    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAdminOrAccountOwner]
    lookup_field = 'username'
    def get_serializer_class(self):

        if self.action in ['list', 'retrieve']:
            return UserDetailsSerializer
        elif self.action in ['create']:
            return UserCreateSerializer
        elif self.action in ['login']:
            return UserLoginSerializer
        return UserDetailsSerializer

    def get_permissions(self):
        action = self.action
        print(action)
        permission_classes = self.permission_classes
        if action in ['list']:
            permission_classes = [IsAdminUser]
        elif action in ['retrieve','update','destroy']:
            permission_classes = [IsAdminOrAccountOwner]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @list_route(methods = ['post'], permission_classes=[AllowAny], url_path = 'login')
    def login(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data = data)

        if serializer.is_valid(raise_exception = True):
            new_data = serializer.data
            return Response(new_data, status = HTTP_200_OK)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
