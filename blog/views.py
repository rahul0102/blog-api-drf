from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from . import forms
# Create your views here.

def articles(request):

    # fetch articles that are published and order by them published date
    articles = Article.objects.exclude(published_date = None).order_by('published_date')
    return render(request, 'blog/articles.html', {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse("article_detail")

    try:

        # get details of only those article that are published
        article = Article.objects.exclude(published_date = None).get(slug=slug)

        # get comments of perticular article

        comments = Comment.objects.filter(approved_comment = True, article=article)
        print("Approve Comments:", comments)
        comment_form = forms.CommentForm()
    except:
        article = None

    user = request.user
    all_comments = Comment.objects.filter(article=article)
    print("ALL Comments:", all_comments)
    if article == None:

        # if current user is author of that unpublished article then he is allowed to see that article
        # print("Non published Article")
        unpublished_article = Article.objects.get(slug=slug)
        unpublished_post_author = unpublished_article.author

        if user == unpublished_post_author:
            article = unpublished_article
            comments = all_comments
        else:
            comments = None
    else:
        if user == article.author:
            comments = all_comments
    print(article)
    print("Comments:", comments)
    return render(request, 'blog/article_details.html', {'article':article, 'comments': comments, 'comment_form': comment_form})

@login_required(login_url = '/account/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArtcile(request.POST, request.FILES)
        author = request.user
        article_instance= form.save(commit=False)
        article_instance.create(author)
        #save to db
        return redirect('articles:my-articles')
    else:
        form = forms.CreateArtcile()
    return render(request, 'blog/article_create.html',{'form': form})

@login_required(login_url = '/account/login/')
def article_publish(request, pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=pk)
        article.publish()
    return redirect('articles:my-articles')

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
def comment_on_article(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        slug = article.slug

        comment_form = forms.CommentForm(request.POST)
        author = request.user.username
        cmnt_instace = comment_form.save(commit=False)
        cmnt_instace.author = author
        cmnt_instace.article = article
        cmnt_instace.save()

    return redirect('/blog/'+slug+'/')

def comment_approve(request,pk):

    try:
        comment = get_object_or_404(Comment, pk=pk)
    except:
        pass
    article = comment.article
    slug = article.slug
    comment.approve()
    comment.save()
    return redirect('/blog/'+slug+'/')

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    article = comment.article
    slug = article.slug
    comment.delete()
    return redirect('/blog/'+slug+'/')
