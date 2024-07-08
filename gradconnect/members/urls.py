from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('mentors/', views.mentor_list, name='mentor_list'),
    path('mentors/<int:id>/', views.mentor_details, name='mentor_details'),
    path('mentors/connect/<int:id>/', views.connect_mentor, name='connect_mentor'),
 
]