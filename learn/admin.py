from django.contrib import admin

from .models import LearnPython, LearnDjango


@admin.register(LearnPython)
class LearnPythonAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'last_updated',
        'main_text',
        ]


@admin.register(LearnDjango)
class LearnDjangoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'last_updated',
        'main_text',
        ]

