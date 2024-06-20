from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """View for the Home Page."""
    template_name = "home.html"


class AboutPageView(TemplateView):
    """View for About Page."""
    template_name = "about.html"


class WebDevView(TemplateView):
    template_name = "webdev.html"

