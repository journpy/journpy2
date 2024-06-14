from django.urls import path, include
from .views import SignUpView

urlpatterns = [
# Include django's default auth urls.
path('', include('django.contrib.auth.urls')),
path('signup/', SignUpView.as_view(), name='signup'),
]