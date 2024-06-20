from django.urls import path
from .views import contact, success

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
]