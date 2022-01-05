import uuid
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.shortcuts import reverse
from django.template.loader import render_to_string
# from core import managers as core_managers

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
    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_GOOGLE = "google"
    LOGIN_FACEBOOK = "facebook"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_GOOGLE, "Google"),
        (LOGIN_FACEBOOK, "Facebook"),
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
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
