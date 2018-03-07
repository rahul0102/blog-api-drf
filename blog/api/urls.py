from django.conf.urls import url
from .views import (
    ArticleCreateAPIView,
    ArticleListAPIView,
    ArticleDetailsAPIView,
    ArticleUpdateAPIView,
    ArticleDeleteAPIView,
    CommentCreateAPIView,
    CommentDetailsAPIView,
    CommentListAPIView,
)
app_name = 'articles-api'
urlpatterns = [
    url(r'^$',ArticleListAPIView.as_view(),name = 'list'),
    url(r'^create/$',ArticleCreateAPIView.as_view(),name = 'create'),
    url(r'^comments/$', CommentListAPIView.as_view(), name = 'comments'),
    url(r'^comments/create/$', CommentCreateAPIView.as_view(), name = 'comments-create'),
    url(r'^comments/(?P<pk>[\w-]+)$', CommentDetailsAPIView.as_view(), name = 'comment-detail'),
    url(r'^(?P<slug>[\w-]+)$',ArticleDetailsAPIView.as_view(),name = 'detail'),
    url(r'^(?P<slug>[\w-]+)/update/$',ArticleUpdateAPIView.as_view(),name = 'update'),
    url(r'^(?P<slug>[\w-]+)/delete/$',ArticleDeleteAPIView.as_view(),name = 'delete'),

]
'''
    curl -X POST http://127.0.0.1:8000/blog/api/articles/comments/create/
    curl -X POST -H "crftoken PrfdnzzVCH2eC1yPK2QkXf7mB1KKCYvkOwFpxuMSChRua37xH7l9rVUMQgv7BugM" http://127.0.0.1:8000/blog/api/articles/comments/create/
'''
