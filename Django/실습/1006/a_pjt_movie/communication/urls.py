from django.urls import path, include
from . import views

app_name = "communication"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
]
