from django import forms
from django.core.validators import EmailValidator
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}), label='')
    email = forms.CharField(validators=[EmailValidator()], label='', widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    #phone = forms.CharField(max_length=15, required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Your Phone Number (optional)'}))
    #subject = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea, label='', help_text='Please keep your message concise and to the point.',)
    captcha = CaptchaField(label='', help_text='Solve the captcha \'*\' is multiplication.')
