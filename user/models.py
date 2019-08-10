from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import MultilingualUserManager


class MultilingualUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image_id = models.ImageField(upload_to="multilingualuser/photos")


    objects = MultilingualUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Language(models.Model):
    first_name = models.CharField(max_length=100)
    language_code = models.CharField(max_length=10)


# - название
# языка
# - код
# языка
