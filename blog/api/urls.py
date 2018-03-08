from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from .views import (
    # ArticleCreateAPIView,
    # ArticleListAPIView,
    # ArticleDetailsAPIView,
    # ArticleUpdateAPIView,
    # ArticleDeleteAPIView,
    # CommentCreateAPIView,
    # CommentDetailsAPIView,
    # CommentListAPIView,
    ArticleViewSet,
    CommentViewSet
)
app_name = 'articles-api'

#######
# Using Router for viewsets
#######
router = DefaultRouter()
router.register('articles', ArticleViewSet, 'articles')
router.register('comments', CommentViewSet, 'comments')
urlpatterns = [
    url(r'^', include(router.urls)),
]
########

#######
# urls for viewsets without router
#######

# urlpatterns = [
#     url(r'^$',ArticleViewSet.as_view({'get': 'list', 'post':'create'}), name = 'list'),
#     url(r'^(?P<slug>[\w-]+)$',ArticleViewSet.as_view({'get': 'retrieve', 'put':'update', 'delete': 'destroy'}), name = 'detail'),
# ]

######
'''
    curl -X POST http://127.0.0.1:8000/blog/api/articles/comments/create/
    curl -X POST -H "crftoken PrfdnzzVCH2eC1yPK2QkXf7mB1KKCYvkOwFpxuMSChRua37xH7l9rVUMQgv7BugM" http://127.0.0.1:8000/blog/api/articles/comments/create/
'''
