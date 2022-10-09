from django.shortcuts import render, redirect
from articles.forms import ArticleForm
from .models import Article


def index(request):
    articles = Article.objects.order_by("-pk")
    content = {
        "articles": articles,
    }
    return render(request, "articles/index.html", content)


def create(request):
    if request.method == "POST":
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            articleForm.save()
            return redirect("articles:index")
    else:
        articleForm = ArticleForm()
    context = {
        "article_form": articleForm,
    }
    return render(request, "articles/new.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/detail.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        articleForm = ArticleForm(request.POST, instance=article)
        if articleForm.is_valid():
            articleForm.save()
            return redirect("articles:detail", article.pk)
    else:
        articleForm = ArticleForm(instance=article)
    context = {
        "article_form": articleForm,
    }
    return render(request, "articles/update.html", context)
