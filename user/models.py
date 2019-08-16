from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from user.managers import MultilingualUserManager
from django.utils.translation import ugettext_lazy as _


class MultilingualUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=40, unique=True)
    is_staff = models.BooleanField(_('is staff'), default=False)
    is_active = models.BooleanField(_('is active'), default=True)
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    position = models.CharField(_('position'), max_length=100)
    image_id = models.ImageField(_('image id'), upload_to="multilingualuser/photos")
    birthday = models.DateField(_('birthday'), null=True )

    objects = MultilingualUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Language(models.Model):
    name = models.CharField(max_length=100)
    language_code = models.CharField(max_length=10)
