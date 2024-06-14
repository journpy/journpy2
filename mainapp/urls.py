from django.urls import path
from .views import (
    HomePageView, AboutPageView, ContactPageView, WebDevView
)

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('webdev', WebDevView.as_view(), name='webdev'),
    path('', HomePageView.as_view(), name='home'),
]