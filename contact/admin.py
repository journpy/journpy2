from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    """Display fields in Django admin."""
    list_display = ['name', 'email', 'phone', 'subject', 'message',]



admin.site.register(Contact, ContactAdmin) 
