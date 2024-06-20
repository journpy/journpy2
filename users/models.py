from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


COURSE_CHOICES = {
    'WEB' : 'Web development with Python',
    'MATH' : 'Python for Mathematics',
    'GAME' : 'Game development with Python',
}


class CustomUser(AbstractUser):
    date_added = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    country = CountryField(blank_label="Select Country")
    course = models.CharField(
        max_length=4, 
        choices=COURSE_CHOICES, 
        default="WEB"
        )