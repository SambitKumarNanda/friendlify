from django.urls import path
from posts import views

urlpatterns = [
    path("create-post/", views.create_post, name="create_post"),
    path("update-post/<id>/", views.update_post, name="update-post"),
    path("delete-post/<id>/", views.delete_post, name="delete-post"),
]
