from django.urls import path
from .views import LearnPythonDetailView, LearnDjangoDetailView

urlpatterns = [
    path('python_tutorial/', LearnPythonDetailView.as_view(), name='python_tutorial'),
    path('django_tutorial/', LearnDjangoDetailView.as_view(), name='django_tutorial'),
    ]