from django.views.generic import ListView
from learn.models.python_models import LearnPython
from learn.models.django_models import LearnDjango


class LearnPythonDetailView(ListView):
    """ List all python tutorials available."""
    model = LearnPython
    paginate_by = 1
    template_name = 'learn/python_tutorial.html'
    context_object_name = 'tutorial_list'


class LearnDjangoDetailView(ListView):
    """ List all Django tutorials available."""
    model = LearnDjango
    template_name = 'learn/django_tutorial.html'
    context_object_name = 'tutorial_list'