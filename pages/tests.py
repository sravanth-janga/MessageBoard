from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.
class PostModelTest(TestCase):
    
    def setUp(self):
        Post.objects.create(text="testing!")
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected = f'{post.text}'
        self.assertEqual(expected,'testing!')

class HomePageViewTest(TestCase):
    def setUP(self):
        Post.objects.create(text="test 2")
    
    def test_view_url_exists(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)

    def test_view_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'home.html')
    

