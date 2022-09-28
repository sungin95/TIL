from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    _todos = Todo.objects.all()
    context = {
        "todos": _todos,
    }

    return render(request, "posts/index.html", context)


def create(request):
    content = request.GET.get("content___")
    Todo.objects.create(content=content)

    return redirect("posts:index")


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("posts:index")
