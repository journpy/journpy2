from django.urls import path
from .views import LearnPythonDetailView

urlpatterns = [
    path('python_tutorial/', LearnPythonDetailView.as_view(), name='python_tutorial'),
    ]