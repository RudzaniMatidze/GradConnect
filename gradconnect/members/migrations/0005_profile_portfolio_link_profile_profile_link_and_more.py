# Generated by Django 5.0.6 on 2024-06-25 23:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_profile_email_profile_name_profile_qualifications_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='portfolio_link',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Portfolio Link'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_link',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Profile Link'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='No bio available', verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Unnamed User', max_length=100, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='qualifications',
            field=models.CharField(default='Not specified', max_length=255, verbose_name='Qualifications'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/', verbose_name='Resume'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(default='No skills listed', max_length=255, verbose_name='Skills'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]