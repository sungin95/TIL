from . import views
from django.urls import path

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("detail/<int:pk>/update", views.update, name="update"),
    path("detail/<int:pk>/delete", views.delete, name="delete"),
    path("detail/<int:pk>/create/", views.create_comment, name="create_comment"),
    path(
        "detail/<int:pk>/comments/<int:comment_pk>/delete/",
        views.comments_delete,
        name="comments_delete",
    ),
]
