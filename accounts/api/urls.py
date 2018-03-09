from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from .views import (
    UserViewSet
)
app_name = 'accounts-api'


schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

#######
# Using Router for viewsets
#######
router = DefaultRouter()
router.register('users', UserViewSet, 'users')
urlpatterns = [
    url(r'^swagger/', schema_view, name="docs"),
    url(r'^', include(router.urls)),
]

#######


#######
# urls for viewsets without router
#######
# urlpatterns = [
#     url(r'^login/$',UserLoginAPIView.as_view(),name = 'login'),
#     url(r'^register/$',UserCreateAPIView.as_view(),name = 'register'),
# ]
#######
