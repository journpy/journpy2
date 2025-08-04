from django.views.generic import ListView, DetailView
from learn.models.python_models import LearnPython
from learn.models.django_models import LearnDjango


class LearnPythonDetailView(ListView):
    """ List all python tutorials available."""
    model = LearnPython
    paginate_by = 1
    template_name = 'learn/python_tutorial.html'
    context_object_name = 'tutorial_list'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     page_number = self.request.GET.get('page', 1)
    #     paginator = self.get_paginator(self.get_queryset(), self.paginate_by)
    #     context['page_number'] = paginator.get_page(page_number)
    #     return context
    

class LearnDjangoDetailView(ListView):
    """ List all Django tutorials available."""
    model = LearnDjango
    template_name = 'learn/django_tutorial.html'
    context_object_name = 'tutorial_list'


class PythonContentView(ListView):
    model = LearnPython
    template_name = 'learn/python_contents.html'
    context_object_name = 'tutorial_list'

    
    
    



    