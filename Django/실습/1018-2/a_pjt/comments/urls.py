from . import views
from django.urls import path

app_name = "comments"

urlpatterns = [
    path("", views.index, name="views"),
]
