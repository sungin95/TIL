from django.urls import path
from . import views

app_name = "articles"


urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("detail/<int:pk>/update", views.update, name="update"),
    path("detail/<int:pk>/delete", views.delete, name="delete"),
    path(
        "detail/<int:artice_pk>/comment_create",
        views.comment_create,
        name="comment_create",
    ),
    path(
        "detail/<int:artice_pk>/comment_delete/<int:comment_pk>",
        views.comment_delete,
        name="comment_delete",
    ),
]
