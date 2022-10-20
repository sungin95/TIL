from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    articles = Article.objects.order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "article_form": form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    article_comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        "article": article,
        "comment_form": comment_form,
        "article_comments": article_comments,
    }
    return render(request, "articles/detail.html", context)


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect("articles:detail", article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            "article_form": form,
        }
        return render(request, "articles/update.html", context)
    else:
        return HttpResponseForbidden()


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            article.delete()
            return redirect("articles:index")
    else:
        return HttpResponseForbidden()


@login_required
def comment_create(request, artice_pk):
    article = Article.objects.get(pk=artice_pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            messages.success(request, "댓글 달기 성공.")
            return redirect("articles:detail", article.pk)
    else:
        return HttpResponseForbidden()


def comment_delete(request, artice_pk, comment_pk):
    article = Article.objects.get(pk=artice_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        if request.method == "POST":
            comment.delete()
            return redirect("articles:detail", article.pk)
    else:
        return HttpResponseForbidden()
