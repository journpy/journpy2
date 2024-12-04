from django.views.generic import ListView
from .models import LearnPython


class LearnPythonDetailView(ListView):
    """ List all python tutorials available."""
    paginate_by = 1
    model = LearnPython
    template_name = 'learn/python_tutorial.html'
    context_object_name = 'tutorial_list'