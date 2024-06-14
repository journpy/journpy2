from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):


    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
        )
        self.post = Post.objects.create(
        title='Post title',
        body='Post content',
        author=self.user,
        )


    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)


    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Post title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Post content')


    def test_post_list_view(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post content')
        self.assertTemplateUsed(response, 'blogs.html')


    def test_post_detail_view(self):
        """Check that a page correctly displays post and its details."""
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Post title')
        self.assertTemplateUsed(response, 'post_detail.html')


