from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    """View for the Home Page."""
    template_name = "mainapp/home.html"


class AboutPageView(TemplateView):
    """View for About Page."""
    template_name = "mainapp/about.html"

