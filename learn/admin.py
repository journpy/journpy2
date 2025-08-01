from django.contrib import admin

from learn.models.python_models import LearnPython
from learn.models.django_models import LearnDjango


@admin.register(LearnPython)
class LearnPythonAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'date_created',
        'date_updated',
        'main_text',
        ]
    def save_model(self, request, obj, form, change):
        """ Override save_model to set the author to the current user. """
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(LearnDjango)
class LearnDjangoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'date_created',
        'date_updated',
        'main_text',
        ]

    def save_model(self, request, obj, form, change):
        """ Override save_model to set the author to the current user. """
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)

