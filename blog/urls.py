from django.conf.urls import url,include
from . import views

app_name = "articles" #namespace for this urls name

urlpatterns = [
    url(r'^articles/$', views.articles, name = 'list'),
    url(r'^create/$', views.article_create, name = 'create'),
    url(r'^my-articles/$', views.user_articles, name = "my-articles"),
    url(r'^(?P<pk>[\d]+)/publish/$', views.article_publish, name = "publish"),
    url(r'^(?P<pk>[\d]+)/remove/$', views.remove_article, name="remove"),
    url(r'^(?P<pk>[\d]+)/comment/$', views.comment_on_article, name="comment"),
    url(r'^comment/(?P<pk>[\d]+)/approve/$', views.comment_approve, name="comment-approve"),
    url(r'^comment/(?P<pk>[\d]+)/delete/$', views.comment_delete, name="comment-delete"),

    # urls for article-api
    url(r'^api/articles/', include('blog.api.urls')),
    url(r'^api/users/', include('accounts.api.urls')),

    # end

    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name = 'details') #\w -> [0-9][a-zA-Z]/s/t etc
]
