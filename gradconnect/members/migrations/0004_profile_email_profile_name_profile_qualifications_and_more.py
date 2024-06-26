# Generated by Django 5.0.6 on 2024-06-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_mentor_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Unnamed User', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='qualifications',
            field=models.CharField(default='Not specified', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='No bio available'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(default='No skills listed', max_length=255),
        ),
    ]
