from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import (
                    CustomUserCreationForm, 
                    CustomUserChangeForm
)
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'first_name', 
        'last_name', 
        'username', 
        'email', 
        'phone_number', 
        'age', 
        'country', 
        'course', 
        'is_staff', 
        'is_superuser', 
        'last_login', 
        'is_active',
        'date_joined',
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
                    'email', 
                    'phone_number', 
                    'age', 
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


admin.site.register(CustomUser, CustomUserAdmin)