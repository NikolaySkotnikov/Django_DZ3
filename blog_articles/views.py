from django.shortcuts import render
from . import dataset


def latest_articles(request):
    context = {'articles': dataset.articles[-3:]}
    return render(request, 'blog_articles/index.html', context)


def all_articles(request):
    context = {'articles': dataset.articles}
    return render(request, 'blog_articles/index.html', context)


def article_details(request, art_slug):
    article = [art for art in dataset.articles if art['slug'] == art_slug]
    return render(request, 'blog_articles/article.html', context=article[0])
