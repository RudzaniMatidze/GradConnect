from django.contrib import admin
from .models import Member, Profile, Mentor

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("jobtitle", "company", "location", "published_date", "job_description")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("get_username", "name", "email", "qualifications", "bio", "skills",)
    search_fields = ("user__username", "name", "email", "skills",)

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'expertise', 'contact_info')
    list_filter = ('expertise',)
    search_fields = ('name', 'expertise', 'contact_info')

