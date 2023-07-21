from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.models import User

# Create your views here.

def homepage(request):
    articles = Article.objects.select_related('author').order_by('-article_id')
    print("Group Content Editor = ",request.user.groups.filter(name='Content-Editor').exists())
    return render(request,"blogs/home.html",{"user":request.user,"articles":articles})

def homepage(request):
    articles = Article.objects.select_related('author').order_by('-article_id')
    print("Group Content Editor = ",request.user.groups.filter(name='Content-Editor').exists())
    return render(request,"blogs/home.html",{"user":request.user,"articles":articles})

def articles_page(request):
    articles = Article.objects.select_related('author').order_by('-article_id')
    print("Group Content Editor = ",request.user.groups.filter(name='Content-Editor').exists())
    return render(request,"blogs/article-list.html",{"user":request.user,"articles":articles})


def article_detail(request,article_id):
    article = Article.objects.select_related('author').get(pk=article_id)
    return render(request,"blogs/article.html",{"user":request,"article":article})

def add_article(request):
    if request.user.groups.filter(name='Content-Editor').exists():
        if request.method == 'POST':
            title = request.POST['title']
            body = request.POST['body']
            author = User.objects.get(username=request.user.username)
            article = Article(title=title,body=body,author=author)
            article.save()
            return redirect('homepage') 
        else:
            form = ArticleForm()
            return render(request,"blogs/add-article.html",{"user":request.user,"form":form})
    else:
        message = "You are unauthorized"
        response = TemplateResponse(request,"blogs/message.html",{"message":message})
        response.status_code = 403
        return response

def edit_article(request,article_id):
    if request.user.groups.filter(name="Content-Editor").exists():
        if request.method == "POST":
            title = request.POST['title']
            body = request.POST['body']
            message = "Artikel berhasil di edit"
            edited_article = Article.objects.get(pk=article_id)
            edited_article.title = title
            edited_article.body = body
            edited_article.save()
            return render(request,"blogs/message.html",{"user":request,"message":message})
        else:
            article = Article.objects.select_related('author').get(pk=article_id)
            edit_form = ArticleForm(initial={
                'title':article.title,
                'author':article.author.username,
                'body':article.body
            })
            edit_form.fields['author'].widget.attrs['readonly'] = True
            return render(request,"blogs/edit-article.html",{"user":request.user,"form":edit_form})
    else:
        message = "You are unauthorized"
        response = TemplateResponse(request,"blogs/message.html",{"message":message})
        response.status_code = 403
        return response