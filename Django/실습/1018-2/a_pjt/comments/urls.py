from . import views
from django.urls import path

app_name = "comments"

urlpatterns = [
    path("create/", views.create, name="create"),
    # path("detail/<int:pk>/update", views.update, name="update"),
    # path("detail/<int:pk>/delete", views.delete, name="delete"),
]
