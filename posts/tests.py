from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    ''' Test for the model/database to check that a text
        is stored correctly '''

    def setUp(self):
        ''' Creates sample database with a single entry '''
        Post.objects.create(text='Just a test.')
    
    def test_text_content(self):
        ''' Checks that the text field of the single database 
            entry is as expected '''
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'Just a test.')


class HomePageViewTest(TestCase):
    ''' Test to evaluate the homepage in terms of:
            Does it actually exist and return a HTTP 200 response? 
            Does it use HomePageView as the view?
            Does it use home.html as the template? 
        'reverse' is used to access the named url 'home'. The url 
            scheme of a project may change over time but the url 
            naming convention will probably not change, so this helps 
            to future-proof the test '''

    def setUp(self):
        Post.objects.create(text='This is another test.')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
