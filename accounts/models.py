from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100, blank=True, default="")
    reset_token = models.CharField(max_length=100, blank=True, default="")
    is_verified = models.BooleanField(default=False)
    is_reset = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
