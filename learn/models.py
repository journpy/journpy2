from django.db import models

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD


class LearnPython(models.Model):
    """ Model a Python tutorial. """
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)
    main_text = MarkdownField(
        rendered_field='main_text_rendered',
        validator=VALIDATOR_STANDARD
        )
    main_text_rendered = RenderedMarkdownField()


    class Meta:
        verbose_name = 'Python Tutorial'
        verbose_name_plural = 'Python Tutorial'


    def __str__(self):
        """ Return a string representation of LearnPython object."""
        return self.title


class LearnDjango(models.Model):
    """ Model a Django tutorial."""
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)
    main_text = MarkdownField(
        rendered_field='main_text_rendered',
        validator=VALIDATOR_STANDARD
        )
    main_text_rendered = RenderedMarkdownField()


    class Meta:
        verbose_name = 'Django Tutorial'
        verbose_name_plural = 'Django Tutorial'


    def __str__(self):
        """ Return a string representation of LearnDjango object."""
        return self.title

