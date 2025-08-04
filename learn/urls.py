from django.urls import path
from learn.views.views import (
    LearnPythonDetailView, 
    LearnDjangoDetailView, 
    PythonContentView, 
)

urlpatterns = [
    path('python_tutorial/', LearnPythonDetailView.as_view(), name='python_tutorial'),
    path('django_tutorial/', LearnDjangoDetailView.as_view(), name='django_tutorial'),
    path('python_contents/', PythonContentView.as_view(), name='python_contents'),
    path('python_tutorial/?page=<int:page_number>/', LearnPythonDetailView.as_view(), name='python-detail'),

    ]