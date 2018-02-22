from django.conf.urls import url
from . import views

app_name = "articles" #namespace for this urls name

urlpatterns = [
    url(r'^articles/$', views.articles, name = 'list'),
    url(r'^create/$', views.article_create, name = 'create'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name = 'details') #\w -> [0-9][a-zA-Z]/s/t etc
]
