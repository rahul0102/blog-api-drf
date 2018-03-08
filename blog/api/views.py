from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .serializers import (
    ArticleListSerializer,
    ArticleDetailSerializer,
    CommentCreateSerializer,
    CommentDetailSerializer,
    CommentListSerializer,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import (
    DestroyModelMixin,
    UpdateModelMixin
)

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from blog.models import Article, Comment
from .pagination import ArticleLimitOffsetPagination,ArticlePageNumberPagination

class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list']:
            return ArticleListSerializer
        return ArticleDetailSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.filter(approved_comment=True)
    serializer_class = CommentListSerializer
    pagination_class = ArticlePageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return CommentDetailSerializer
        elif self.action in ['create']:
            return CommentCreateSerializer
        return CommentListSerializer

    def create(self, request):

        print(request.data)
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save(author = request.user)
            return Response(serializer.validated_data, status = HTTP_201_CREATED)

        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

class ArticleDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    lookup_field = 'slug'

class ArticleDetailsAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

    lookup_field = 'slug'

class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    pagination_class = ArticlePageNumberPagination

class ArticleUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = ArticleListSerializer
    lookup_field = 'slug'

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentDetailsAPIView(DestroyModelMixin, UpdateModelMixin,RetrieveAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.filter(approved_comment=True)
    serializer_class = CommentListSerializer
    pagination_class = ArticlePageNumberPagination
