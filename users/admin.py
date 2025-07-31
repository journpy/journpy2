from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import (
                    CustomUserCreationForm, 
                    CustomUserChangeForm,
)
from .models import CustomUser
from django.db import models
from journpy2.widgets import PastCustomDatePickerWidget


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    formfield_overrides = {
        models.DateField:{'widget': PastCustomDatePickerWidget},

    }
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'first_name', 
        'last_name', 
        'username', 
        'date_of_birth',
        'email', 
        'phone_number', 
        'country', 
        'course', 
        'is_staff', 
        'is_superuser', 
        'last_login', 
        'is_active',
        'date_joined',
        'reference_code',
        ]
    list_filter = [
        'email', 
        'is_staff', 
        'is_active',
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    'first_name', 
                    'last_name', 
                    'username', 
                    'date_of_birth',
                    'email', 
                    'phone_number',  
                    'country', 
                    'course',
                    'password1',
                    'password2',
                ],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []