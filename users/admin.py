from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name', 'username', 'email', 
        'date_added', 'phone_number', 'age', 'country', 'course', 'is_staff', 
        'is_superuser', 'last_login', 'is_active',]


admin.site.register(CustomUser, CustomUserAdmin)