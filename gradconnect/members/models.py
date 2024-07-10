from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.apps import AppConfig


# Define the Member model representing job postings
class Member(models.Model):
    jobtitle = models.CharField(max_length=255)  # Job title of the member
    company = models.CharField(max_length=255)  # Company name
    location = models.CharField(max_length=255, default="Unknown")  # Job location
    email = models.EmailField(null=True)  # Email contact for the job
    published_date = models.DateField(null=True)  # Date when the job was published
    job_description = models.TextField(null=True, blank=True)  # Description of the job

    def __str__(self):
        return f"{self.jobtitle} {self.location}"  # String representation of the Member object


# Define the Profile model representing user profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")  # Link to the User model
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name="Profile Picture")  # Profile picture
    name = models.CharField(max_length=100, default='Unnamed User', verbose_name="Full Name")  # Full name of the user
    email = models.EmailField(default='example@example.com', verbose_name="Email Address")  # Email address
    qualifications = models.CharField(max_length=255, default='Not specified', verbose_name="Qualifications")  # User's qualifications
    bio = models.TextField(default='No bio available', verbose_name="Bio")  # User's bio
    skills = models.CharField(max_length=255, default='No skills listed', verbose_name="Skills")  # User's skills
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, verbose_name="Resume")  # Uploaded resume
    portfolio_link = models.URLField(max_length=255, blank=True, null=True, verbose_name="Portfolio Link")  # Link to the user's portfolio
    profile_link = models.URLField(max_length=255, blank=True, null=True, verbose_name="Profile Link")  # Link to the user's profile

    def __str__(self):
        return f'{self.user.username} Profile'  # String representation of the Profile object


# Define the Mentor model representing mentors
class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to the User model
    name = models.CharField(max_length=255)  # Mentor's name
    expertise = models.CharField(max_length=255)  # Mentor's expertise
    contact_info = models.CharField(max_length=255)  # Mentor's contact information
    bio = models.TextField(blank=True)  # Mentor's bio
    profile_pic = models.ImageField(upload_to='mentor_profile_pics/', blank=True)  # Mentor's profile picture

    def __str__(self):
        return self.name  # String representation of the Mentor object


# Define the Application model representing job applications
class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('review', 'Review'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    job = models.ForeignKey(Member, on_delete=models.CASCADE)  # Link to the Member model
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='applied')  # Status of the application
    date = models.DateTimeField(auto_now_add=True)  # Date when the application was created

    def __str__(self):
        return f"{self.user.username} - {self.job.jobtitle}"  # String representation of the Application object


# Define the app configuration class
class YourAppConfig(AppConfig):
    name = 'members'  # Name of the app

    def ready(self):
        import members.signals  # Import signals module when the app is ready
