from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # User signup page
    path('signup/', views.signup_view, name='signup'),
    
    # Profile creation page
    path('create_profile/', views.create_profile, name='create_profile'),
    
    # User login page
    path('login/', views.login_view, name='login'),
    
    # User logout functionality
    path('logout/', views.logout_view, name='logout'),
    
    # Members listing page
    path('members/', views.members, name='members'),
    
    # Member details page, requires a member id
    path('members/details/<int:id>', views.details, name='details'),
    
    # User profile page
    path('profile/', views.profile, name='profile'),
    
    # Edit user profile page
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    
    # Mentor listing page
    path('mentors/', views.mentor_list, name='mentor_list'),
    
    # Mentor details page, requires a mentor id
    path('mentors/<int:id>/', views.mentor_details, name='mentor_details'),
    
    # Connect with a mentor, requires a mentor id
    path('mentors/connect/<int:id>/', views.connect_mentor, name='connect_mentor'),
]
