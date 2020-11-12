from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username: models.CharField = models.CharField(
        "username", max_length=30, unique=True
    )
    first_name: models.CharField = models.CharField("first name", max_length=30)
    last_name: models.CharField = models.CharField("last name", max_length=30)
    email: models.EmailField = models.EmailField("email", unique=True)
    is_admin: models.BooleanField = models.BooleanField(default=False)
    is_staff: models.BooleanField = models.BooleanField(default=False)
    is_active: models.BooleanField = models.BooleanField(default=True)
    date_joined: models.DateField = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    objects = UserManager()

    def __str__(self):
        return f"<User: {self.id}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
