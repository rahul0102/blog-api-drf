from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from . import forms
# Create your views here.

def articles(request):

    articles = Article.objects.all().order_by('published_date')

    return render(request, 'blog/articles.html', {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse("article_detail")
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/article_details.html', {'article':article})

@login_required(login_url = '/account/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArtcile(request.POST, request.FILES)
        author = request.user
        article_instance= form.save(commit=False)
        article_instance.publish(author)
        #save to db
        return redirect('articles:list')
    else:
        form = forms.CreateArtcile()
    return render(request, 'blog/article_create.html',{'form': form})

@login_required(login_url = '/account/login/')
def user_articles(request):
    # get articles of perticular user
    author = request.user
    articles = Article.objects.filter(author=author)
    return render(request, 'blog/user_articles.html',{'articles': articles})

def remove_article(request,pk):
    if request.method == 'POST':
        # Delete the article of user
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    else:
        pass
    return redirect('articles:my-articles')
