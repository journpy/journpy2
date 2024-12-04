from django.views.generic import ListView
from .models import LearnPython, LearnDjango


class LearnPythonDetailView(ListView):
    """ List all python tutorials available."""
    paginate_by = 1
    model = LearnPython
    template_name = 'learn/python_tutorial.html'
    context_object_name = 'tutorial_list'


class LearnDjangoDetailView(ListView):
    """ List all Django tutorials available."""
    model = LearnDjango
    template_name = 'learn/django_tutorial.html'
    context_object_name = 'tutorial_list'