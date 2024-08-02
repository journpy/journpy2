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
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    country = CountryField(blank_label="Select Country")
    course = models.CharField(
        max_length=4, 
        choices=COURSE_CHOICES, 
        default="SEL"
        )
    # Make email the default for logging in
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']