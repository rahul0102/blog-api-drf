from django.conf.urls import url
from .views import (
    UserCreateAPIView,
    UserLoginAPIView
)
app_name = 'accounts-api'
urlpatterns = [
    url(r'^login/$',UserLoginAPIView.as_view(),name = 'login'),
    url(r'^register/$',UserCreateAPIView.as_view(),name = 'register'),
    # url(r'^comments/$', CommentListAPIView.as_view(), name = 'comments'),
    # url(r'^comments/create/$', CommentCreateAPIView.as_view(), name = 'comments-create'),
    # url(r'^comments/(?P<pk>[\w-]+)$', CommentDetailsAPIView.as_view(), name = 'comment-detail'),
    # url(r'^(?P<slug>[\w-]+)$',ArticleDetailsAPIView.as_view(),name = 'detail'),
    # url(r'^(?P<slug>[\w-]+)/update/$',ArticleUpdateAPIView.as_view(),name = 'update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$',ArticleDeleteAPIView.as_view(),name = 'delete'),
]
