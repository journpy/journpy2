from django.db import models

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD


class Post(models.Model):
    """Model a blog post."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,)
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    # Implementing django-markdownfield 
    body = MarkdownField(
        rendered_field='body_rendered', 
        validator=VALIDATOR_STANDARD
        )
    body2 = MarkdownField(
        rendered_field='body2_rendered', 
        validator=VALIDATOR_STANDARD
        )
    body_rendered = RenderedMarkdownField()
    body2_rendered = RenderedMarkdownField()

    imgname = models.CharField(max_length=250, blank=True)
    imgname2 = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    image2 = models.ImageField(upload_to='images/', blank=True)
    slug = models.SlugField(max_length=255)

    
    class Meta:
        ordering = ('-date_created',)


    def __str__(self):
        """Return a string representation of the object."""
        return self.title.capitalize()
