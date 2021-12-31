from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    """ Custom User Model """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
    )
    LANGUAGE_BENGALI = "bd"
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_BENGALI, "Bangla")
    )

    CURRENCY_BDT = "bdt"
    CURRENCY_USD = "usd"

    CURRENCY_CHOICES = (
        (CURRENCY_BDT, "BDT"),
        (CURRENCY_USD, "USD")
    )

    avatar = models.ImageField(null=True, blank=True)
    # null=True is for database, blank=True is for admin form
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True)
    superhost = models.BooleanField(default=False)
