from django.contrib import admin
from models import JobLocation, SalaryRange, Hour, EmploymentType, SpecialCondition
from models import Job, Essential, Desireable
__author__ = 'ir4y'


class EssentialTabInline(admin.TabularInline):
    model = Essential


class DesireableTabInline(admin.TabularInline):
    model = Desireable


class JobAdmin(admin.ModelAdmin):
    inlines = (EssentialTabInline, DesireableTabInline)

admin.site.register(Job, JobAdmin)
admin.site.register(JobLocation)
admin.site.register(SalaryRange)
admin.site.register(Hour)
admin.site.register(EmploymentType)
admin.site.register(SpecialCondition)