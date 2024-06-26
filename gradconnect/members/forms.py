from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'name', 'email', 'qualifications', 'bio', 'skills', 'resume', 'portfolio_link', 'profile_link']
        labels = {
            'profile_pic': 'Profile Picture',
            'name': 'Full Name',
            'email': 'Email Address',
            'qualifications': 'Qualifications',
            'bio': 'Bio',
            'skills': 'Skills',
            'resume': 'Resume',
            'portfolio_link': 'Portfolio Link',
            'profile_link': 'Profile Link',
        }
        widgets = {
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'qualifications': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'List your qualifications'}),
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter comma-separated values'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'portfolio_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your portfolio link'}),
            'profile_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your profile link'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_skills(self):
        skills = self.cleaned_data.get('skills', '')
        if not skills:
            return skills
        skills_list = [skill.strip() for skill in skills.split(',')]
        return ', '.join(skills_list)

class JobSearchForm(forms.Form):
    query = forms.CharField(
        label='Search',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search jobs or companies...'
        })
    )