from django.test import SimpleTestCase
from django.urls import reverse

class MainAppTests(SimpleTestCase):


    def test_home_page_view(self):
        """Test for HomePageView."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


    def test_contact_page_view(self):
        """Test for ContactPageView."""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    
    def test_about_page_view(self):
        """Test for AboutPageView."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    

