from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Member, Profile, Mentor, Application
from datetime import datetime

class ViewsTestCase(TestCase):

    def setUp(self):
        # Set up test data and a test client
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user, bio='Test bio')
        self.member = Member.objects.create(name='Test Member', description='Test Description')
        self.mentor = Mentor.objects.create(name='Test Mentor', expertise='Test Expertise')
        self.application = Application.objects.create(user=self.user, job=self.member, date=datetime.now(), status='applied')
        
    def test_home_view(self):
        # Test home view
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        
    def test_signup_view_get(self):
        # Test signup view with GET request
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_view_post(self):
        # Test signup view with POST request
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful sign up

    def test_login_view_get(self):
        # Test login view with GET request
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post(self):
        # Test login view with POST request
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login

    def test_logout_view(self):
        # Test logout view
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logout.html')

    def test_profile_view(self):
        # Test profile view for logged-in user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_edit_profile_view_get(self):
        # Test edit profile view with GET request for logged-in user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_profile.html')

    def test_edit_profile_view_post(self):
        # Test edit profile view with POST request for logged-in user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('edit_profile'), {
            'bio': 'Updated bio'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful profile update

    def test_mentor_list_view(self):
        # Test mentor list view
        response = self.client.get(reverse('mentor_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mentor.html')

    def test_mentor_details_view(self):
        # Test mentor details view
        response = self.client.get(reverse('mentor_details', args=[self.mentor.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mentor_details.html')

    def test_connect_mentor_view(self):
        # Test connect mentor view for logged-in user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('connect_mentor', args=[self.mentor.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after connecting with mentor

    def test_members_view(self):
        # Test members view
        response = self.client.get(reverse('members'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs.html')

    def test_details_view(self):
        # Test member details view
        response = self.client.get(reverse('details', args=[self.member.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'details.html')

    def test_create_profile_view_get(self):
        # Test create profile view with GET request for logged-in user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_profile.html')

    def test_create_profile_view_post(self):
        # Test create profile view with POST request for logged-in user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('create_profile'), {
            'bio': 'New bio'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful profile creation
 