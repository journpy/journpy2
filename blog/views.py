from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.conf import settings


class BlogListView(ListView):
    """Show a list of blogs.""" 
    model = Post
    template_name = 'blogs.html'
    context_object_name = 'post_list'
    

class BlogDetailView(LoginRequiredMixin, AccessMixin, DetailView):
    """ Show a blog and its entry. """
    model = Post
    template_name = 'post_detail.html'
    login_url = settings.LOGIN_REDIRECT_URL



