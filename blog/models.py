from django.db import models
from django.conf import settings
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD


class Post(models.Model):
    """Model a blog post."""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_superuser': True},
        )
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    # Implementing django-markdownfield
    body = MarkdownField(
        rendered_field='body_rendered',
        validator=VALIDATOR_STANDARD,
        )
    body_rendered = RenderedMarkdownField()
    image_name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    slug = models.SlugField(max_length=100)


    class Meta:
        ordering = ('-date_created',)


    def __str__(self):
        """Return a string representation of the object."""
        return self.title.capitalize()
