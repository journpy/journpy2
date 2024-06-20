from django.urls import path
from .views import (
    HomePageView, AboutPageView, WebDevView
)

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('webdev', WebDevView.as_view(), name='webdev'),
    path('', HomePageView.as_view(), name='home'),
]