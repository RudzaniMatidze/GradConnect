from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    jobtitle = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default="Unknown")
    email = models.EmailField(null=True)
    published_date = models.DateField(null=True)

def __str__(self):
    return f"{self.jobtitle} {self.location}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name="Profile Picture")
    name = models.CharField(max_length=100, default='Unnamed User', verbose_name="Full Name")
    email = models.EmailField(default='example@example.com', verbose_name="Email Address")
    qualifications = models.CharField(max_length=255, default='Not specified', verbose_name="Qualifications")
    bio = models.TextField(default='No bio available', verbose_name="Bio")
    skills = models.CharField(max_length=255, default='No skills listed', verbose_name="Skills")
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, verbose_name="Resume")
    portfolio_link = models.URLField(max_length=255, blank=True, null=True, verbose_name="Portfolio Link")
    profile_link = models.URLField(max_length=255, blank=True, null=True, verbose_name="Profile Link")

    def __str__(self):
        return self.name

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    expertise = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='mentor_profile_pics/', blank=True)

    def __str__(self):
        return self.name