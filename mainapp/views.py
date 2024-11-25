from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    """View for the Home Page."""
    template_name = "home.html"


class AboutPageView(TemplateView):
    """View for About Page."""
    template_name = "about.html"


class WebDevView(LoginRequiredMixin, AccessMixin, TemplateView):
    template_name = "webdev.html"
    login_url = reverse_lazy('login')


class BootCampView(TemplateView):
    template_name = 'bootcamps.html'

