from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'gender',
        'title',
        'address',
        'email',
        'social',
        'number',
        'objective',
        'company_name',
        'job_title',
        'job_date_form',
        'job_date_to',
        'college_name',
        'course',
        'gpa',
        'skills',
        'profile_picture')