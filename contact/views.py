from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            #phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            EmailMessage(
                subject='Contact Form Submission from {}'.format(name),
                body=f'{message}',
                from_email='form-response@example.com', # Send from (your website)
                to=['journpy@gmail.com'], # Send to (your admin email)
                bcc=[],
                reply_to=[email] # Email from the form to get back to
                ).send()

            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def success(request):
    return render(request, 'contact/success.html')
