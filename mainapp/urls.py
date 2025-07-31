from django.urls import path
from .views import (
    HomePageView, AboutPageView, WebDevView, BootCampView,
)

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('bootcamps/', BootCampView.as_view(), name='bootcamps'),
    path('webdev', WebDevView.as_view(), name='webdev'),
    path('', HomePageView.as_view(), name='home'),
]