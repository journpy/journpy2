from django.db import models
from django.core.validators import EmailValidator

class Contact(models.Model):
    """Model a contact form."""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        """Return a string representation of a contact object."""
        return self.message
