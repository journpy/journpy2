from django.contrib import admin
from .models import Contact
from .forms import ContactForm


class ContactAdmin(admin.ModelAdmin):
    """Display fields in Django admin."""
    add_form = ContactForm
    list_display = [
        'name', 
        'email', 
        'phone', 
        'subject', 
        'message',        
        ]
admin.site.register(Contact, ContactAdmin) 
