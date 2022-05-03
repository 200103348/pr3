from django.test import TestCase

# Create your tests here.

class testing(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_firstpage(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_secondpage(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)