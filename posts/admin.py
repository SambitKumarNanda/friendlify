from django.contrib import admin
from posts.models import UserPostsModel,UserSavedPostModel

# Register your models here.

admin.site.register(UserPostsModel)
admin.site.register(UserSavedPostModel)