from django.shortcuts import render, redirect

# Create your views here.
def create(request):

    return redirect("articles:index")
