from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member, Profile, Mentor, Application
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProfileForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from datetime import datetime


# View to list all Jobs 
def members(request):
    jobs = Member.objects.all().values()

    # Application progress for the logged-in user
    if request.user.is_authenticated:
        current_month = datetime.now().month
        applications = Application.objects.filter(user=request.user, date__month=current_month)
        
        application_progress = {
            'total_applied': applications.count(),
            'interview': applications.filter(status='interview').count(),
            'review': applications.filter(status='review').count(),
            'rejected': applications.filter(status='rejected').count(),
            'accepted': applications.filter(status='accepted').count(),
        }
    else:
        application_progress = None

    template = loader.get_template('jobs.html')
    context = {
        'jobs': jobs,
        'application_progress': application_progress,
    }
    return HttpResponse(template.render(context, request))


# View to show details of a specific member
def details(request, id):
    jobs = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'jobs': jobs,
    }
    return HttpResponse(template.render(context, request))


# Home page view
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


# Profile view for logged-in users
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


# View to edit profile for logged-in users
@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'edit_profile.html', context)


# View to list all mentors
def mentor_list(request):
    mentors = Mentor.objects.all()
    return render(request, 'mentor.html', {'mentors': mentors})


# View to show details of a specific mentor
def mentor_details(request, id):
    mentor = get_object_or_404(Mentor, id=id)
    return render(request, 'mentor_details.html', {'mentor': mentor})


# View to connect with a mentor
def connect_mentor(request, id):
    mentor = get_object_or_404(Mentor, id=id)
   
    # Redirect back to the mentors list after connecting
    return redirect('mentor_list')


# Logout view
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Sign-up view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('create_profile')  # Redirect to profile creation page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# View to create profile for logged-in users
@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})