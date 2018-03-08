from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet
)
app_name = 'accounts-api'

#######
# Using Router for viewsets
#######
router = DefaultRouter()
router.register('users', UserViewSet, 'users')
urlpatterns = [
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
