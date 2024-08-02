from django.db import models

class Post(models.Model):
    """Model a blog post."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,)
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    body2 = models.TextField()
    imgname = models.CharField(max_length=250, blank=True)
    imgname2 = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    image2 = models.ImageField(upload_to='images/', blank=True)
    slug = models.SlugField(max_length=255)


    def __str__(self):
        """Return a string representation of the object."""
        return self.title.capitalize()
