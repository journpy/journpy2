from django.urls import path
from .views import (
    BlogListView, BlogDetailView,
)

urlpatterns = [
path('post/<int:pk>/<slug:slug>/', BlogDetailView.as_view(), name='post_detail'), 
path('blogs/', BlogListView.as_view(), name='blogs'),

]