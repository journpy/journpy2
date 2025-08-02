from django import forms
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,)
from .models import CustomUser
from datetime import date


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges.
    """

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'first_name', 
            'last_name', 
            'username', 
            'date_of_birth',
            'email', 
            'phone_number', 
            'country', 
            'course',
            )
        widgets = {
            'date_of_birth':forms.widgets.DateInput(attrs={
                'type': 'date', 
                'max': date.today(),
                'min': date(1900, 1, 1),
                })

        }


class CustomUserChangeForm(UserChangeForm):


    class Meta:
        model = CustomUser
        fields = (
            'first_name', 
            'last_name', 
            'username', 
            'date_of_birth',
            'email', 
            'phone_number', 
            'country', 
            'course',
        )


