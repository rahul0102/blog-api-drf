# from rest_framework.generics import (
#     CreateAPIView,
#     ListAPIView,
#     RetrieveAPIView,
#     RetrieveUpdateAPIView,
#     UpdateAPIView,
#     DestroyAPIView,
# )
from .serializers import (
    ArticleListSerializer,
    ArticleDetailSerializer,
    CommentCreateSerializer,
    CommentDetailSerializer,
    CommentListSerializer,
)
from rest_framework.viewsets import ModelViewSet
# from rest_framework.mixins import (
#     DestroyModelMixin,
#     UpdateModelMixin
# )

from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from blog.models import Article, Comment
from .pagination import ArticleLimitOffsetPagination,ArticlePageNumberPagination

class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleDetailSerializer
    pagination_class = ArticlePageNumberPagination
    queryset = Article.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly ]

    def get_serializer_class(self):
        if self.action in ['list']:
            return ArticleListSerializer
        return ArticleDetailSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.filter(approved_comment=True)
    serializer_class = CommentDetailSerializer
    pagination_class = ArticlePageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list']:
            return CommentListSerializer
        elif self.action in ['create']:
            return CommentCreateSerializer
        return CommentDetailSerializer

    def create(self, request):
        print(request.data)
        serializer = CommentCreateSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save(author = self.request.user)
            return Response(serializer.data, status = HTTP_201_CREATED)

        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
