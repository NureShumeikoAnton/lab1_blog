from django.shortcuts import render
from .models import Article

def articles_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/articles_list.html', context)

def articles_by_author(request, author_name):
    articles = Article.objects.filter(author=author_name)
    context = {
        'author_name': author_name,
        'articles': articles
    }
    return render(request, 'articles/author_articles.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {'article': article}
    return render(request, 'articles/article_detail.html', context)
