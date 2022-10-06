from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movie = Movie.objects.order_by("-pk")
    context = {
        "movies": movie,
    }
    return render(request, "communication/index.html", context)


def create(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("communication:index")
    else:
        movie_form = MovieForm()
    context = {
        "movie_form": movie_form,
    }
    return render(request, "communication/create.html", context)


def new(request, pk):
    select_movie = Movie.objects.get(pk=pk)
    context = {
        "movie": select_movie,
    }
    return render(request, "communication/new.html", context)


def update(request, pk):
    select_movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie_form = MovieForm(request.POST, instance=select_movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("communication:index")
    else:
        movie_form = MovieForm(instance=select_movie)
    context = {
        "movie_form": movie_form,
    }
    return render(request, "communication/update.html", context)


def delete(request, pk):
    select_movie = Movie.objects.get(pk=pk)
    select_movie.delete()
    return redirect("communication:index")
