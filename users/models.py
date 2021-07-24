from django.contrib.auth.models import AbstractUser
from django.db import models
from . import choices

# Create your models here.


class User(AbstractUser):

    """custom user model"""

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, null=True, choices=choices.GENDER_CHOICES, blank=True
    )
    bio = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    language = models.CharField(
        max_length=20, blank=True, choices=choices.LANGUAGE_CHOICES
    )
    currency = models.CharField(
        max_length=20, blank=True, choices=choices.CURRENCY_CHOICES
    )
