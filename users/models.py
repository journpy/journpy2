import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


COURSE_CHOICES = {
    'SEL' : '--- Select Course ---',
    'WEB' : 'Web development with Python',
    'BOOT' : 'Python Bootcamp',
    'MATH' : 'Python for Mathematics',
    'GAME' : 'Game development with Python',
}


class CustomUser(AbstractUser):
    """ Custom user model. """
    id = models.UUIDField(
        default=uuid.uuid4, 
        primary_key=True, 
        unique=True, 
        editable=False,
        )
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(
        blank=True,
        help_text="Enter phone number with country code e.g. +234XXXXXXXXXX",
        )
    country = CountryField(blank_label="Select Country")
    course = models.CharField(
        max_length=4,
        choices=COURSE_CHOICES,
        default="SEL",
        )
    reference_code = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    # Make email the default for logging in
    USERNAME_FIELD = 'email'
    # Ask for these when creating superuser
    REQUIRED_FIELDS = ['username', 'date_of_birth']

