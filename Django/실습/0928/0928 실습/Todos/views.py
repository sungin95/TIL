from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    _todos = Todo.objects.all()
    context = {"todos": _todos}

    return render(request, "todos/index.html", context)


def create(request):
    todo__work = request.GET.get("todo__work")
    todo__priority = request.GET.get("todo__priority")
    todo__deadline = request.GET.get("todo__deadline")
    todo__state = request.GET.get("todo__state")
    print(type(todo__work))
    Todo.objects.create(
        content=todo__work,
        priority=todo__priority,
        deadline=todo__deadline,
        completed=todo__state,
    )
    return redirect("todos:index")


def delete(request, todo_pk):
    clicked_id = Todo.objects.get(pk=todo_pk)
    clicked_id.delete()

    return redirect("todos:index")


def modify(request, todo_pk):
    clicked_id = Todo.objects.get(pk=todo_pk)
    if clicked_id.completed == False:
        clicked_id.completed = True
        clicked_id.save()
    else:
        clicked_id.completed = False
        clicked_id.save()
    return redirect("todos:index")
