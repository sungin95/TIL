from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.
def index(request):
    all_ = Articles.objects.all()
    content = {
        "contents": all_,
    }
    return render(request, "articles/index.html", content)


def edit(request):

    return render(request, "articles/edit.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Articles.objects.create(
        title=title,
        content=content,
    )
    return redirect("articles:index")
