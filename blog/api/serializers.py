from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from accounts.api.serializers import UserDetailsSerializer

from blog.models import Article, Comment

class ArticleListSerializer(ModelSerializer):
    article_url = HyperlinkedIdentityField(
        view_name='articles:articles-api:articles-detail',
        lookup_field='slug'
    )
    author = SerializerMethodField()
    comments_count = SerializerMethodField()
    class Meta:
        model = Article
        fields = [
            'article_url',
            'title',
            'text',
            'author',
            'comments_count',
        ]
    def get_author(self, obj):
        return str(obj.author.username)

    def get_comments_count(self, obj):
        return obj.comments.count()

class ArticleDetailSerializer(ModelSerializer):
    author = UserDetailsSerializer(read_only = True)
    comments = SerializerMethodField()
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'slug',
            'text',
            'thumbnail',
            'author',
            'comments'
        ]
    # def get_author(self, obj):
    #     return str(obj.author.username)

    def get_comments(self,obj):
        return CommentDetailSerializer(obj.comments.all(), many=True).data

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'article',
            'text',
        ]
class CommentDetailSerializer(ModelSerializer):
    article = SerializerMethodField()
    # author = UserDetailsSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = [
            'id',
            'article',
            # 'article_url',
            'author',
            'text',
            'created_date',

        ]
        read_only_fields = [
            'article',
            'author',
        ]
    def get_article(self, obj):
        print("Obj", obj)
        return obj.article.slug

class CommentListSerializer(ModelSerializer):
    comment_url = HyperlinkedIdentityField(
        view_name='articles:articles-api:comments-detail',
    )
    article = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'comment_url',
            'article',
            # 'article_url',
            'author',
            'text',
        ]
    def get_article(self, obj):
        return str(obj.article.slug)

"""
from blog.models import Article
from blog.api.serializers import ArticleDetailSerializer


data = {
    "title" : "test",
    "text": "test 12334"
    "slug":"test-1"
}

new_item = ArticleDetailSerializer(data = data)
if new_item.is_valid():
    new_item.save()
else:

"""
