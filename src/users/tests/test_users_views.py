
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.username = "testuser"
        self.password = "testpassword123"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_view_get(self):
        # Test GET request to login view
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views/login.html')
        self.assertIsInstance(response.context['login_form'], AuthenticationForm)

    def test_login_view_post_valid(self):
        # Test POST request with valid credentials
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, reverse('home'))
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_view_post_invalid(self):
        # Test POST request with invalid credentials
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views/login.html')
        self.assertContains(response, 'Invalid username or password')

    def test_logout_view(self):
        # Test logout functionality
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/')
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_register_view_get(self):
        # Test GET request to register view
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views/register.html')
        self.assertIsInstance(response.context['register_form'], UserCreationForm)

    def test_register_view_post_valid(self):
        # Test POST request with valid registration data
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_register_view_post_invalid(self):
        # Test POST request with invalid registration data
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views/register.html')
        self.assertContains(response, 'Please retry registration')
        self.assertFalse(User.objects.filter(username='newuser').exists())