from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member, Profile, Mentor
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout
from .forms import ProfileForm
from django.contrib import messages


# Create your views here.
def members(request):
    jobs = Member.objects.all().values()
    template = loader.get_template('jobs.html')
    context = {
        'jobs': jobs,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    jobs = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'jobs': jobs,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


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
    return render(request, 'edit_profile.html', {'form': form})

def mentor_list(request):
    mentors = Mentor.objects.all()
    return render(request, 'mentor.html', {'mentors': mentors})

def mentor_details(request, id):
    mentor = get_object_or_404(Mentor, id=id)
    return render(request, 'mentor_details.html', {'mentor': mentor})

def connect_mentor(request, id):
    mentor = get_object_or_404(Mentor, id=id)
    # Implement your connection logic here (e.g., send connection request)
    # For example, you can add the current user to a list of mentees of the mentor

    # Redirect back to the mentors list after connecting
    return redirect('mentor_list')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')
