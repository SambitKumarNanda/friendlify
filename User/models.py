from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here.

class UsersProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="users_profile_model_user")
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="user-profile/", null=True, blank="True")
    bio = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)  # https://wa.me/phone_no
    gmail = models.EmailField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)



