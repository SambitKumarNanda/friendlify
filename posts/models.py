from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class UserPostsModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True,
                             related_name="user_post_model_user")
    title = models.CharField(max_length=300, null=True, blank=True)
    media = models.ImageField(upload_to="user-posts/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(get_user_model(), related_name="users_post_model_likes", blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class UserSavedPostModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="users_saved_post_model_user")
    posts = models.ManyToManyField(UserPostsModel, related_name="user_saved_posts", blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
