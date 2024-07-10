from django.contrib import admin
from .models import Member, Profile, Mentor


# Register the Member model with the admin site using a custom admin class
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("jobtitle", "company", "location", "published_date", "job_description")  # Fields to display in the list view


# Register the Profile model with the admin site using a custom admin class
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("get_username", "name", "email", "qualifications", "bio", "skills")  # Fields to display in the list view
    search_fields = ("user__username", "name", "email", "skills")  # Fields to include in the search functionality

    # Custom method to display the username of the related User object
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'  # Set the column header for the custom method


# Register the Mentor model with the admin site using a custom admin class
@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'expertise', 'contact_info')  # Fields to display in the list view
    list_filter = ('expertise',)  # Fields to include in the filter sidebar
    search_fields = ('name', 'expertise', 'contact_info')  # Fields to include in the search functionality


