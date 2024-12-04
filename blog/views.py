from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    """Show a list of blogs."""
    model = Post
    template_name = 'blog/blogs.html'
    context_object_name = 'post_list'


class BlogDetailView(DetailView):
    """ Show a blog and its entry. """
    model = Post
    template_name = 'blog/post_detail.html'



