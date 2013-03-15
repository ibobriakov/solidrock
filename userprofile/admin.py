from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import Employer, JobSeeker, JobSeekerInformation, JobSeekerCurrentEmployment, JobSeekerPreviousEmployment,\
                   JobSeekerEducationType, JobSeekerEducation, JobSeekerReferee
from userprofile.forms import CustomUserChangeForm

__author__ = 'ir4y'

admin.site.unregister(User)


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'user_type', 'is_email_active', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class JobSeekerPreviousEmploymentTabInline(admin.StackedInline):
    model = JobSeekerPreviousEmployment


class JobSeekerEducationTabInline(admin.TabularInline):
    model = JobSeekerEducation


class JobSeekerRefereeTabInline(admin.StackedInline):
    model = JobSeekerReferee


class JobSeekerAdmin(admin.ModelAdmin):
    inlines = (JobSeekerPreviousEmploymentTabInline, JobSeekerEducationTabInline, JobSeekerRefereeTabInline)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Employer)
admin.site.register(JobSeeker, JobSeekerAdmin)
admin.site.register(JobSeekerInformation)
admin.site.register(JobSeekerCurrentEmployment)
admin.site.register(JobSeekerEducationType)

