from django.db import models
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
from django.conf import settings


class BaseTutorial(models.Model):
    """ Model a tutorial. """
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    main_text = MarkdownField(
        rendered_field='main_text_rendered',
        validator=VALIDATOR_STANDARD
        )
    main_text_rendered = RenderedMarkdownField()

    def __str__(self):
        """ Return a string representation of LearnPython object."""
        return self.title.title()

    class Meta:
        abstract = True

