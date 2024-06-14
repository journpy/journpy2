from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges.
    """

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'username', 'email', 
            'phone_number', 'age', 'country', 'course',
            )


class CustomUserChangeForm(UserChangeForm):


    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'username', 'email', 
            'phone_number', 'age', 'country', 'course',
        )