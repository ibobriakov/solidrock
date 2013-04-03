from django.contrib import admin
from models import JobLocation, JobArea,  SalaryRange, Hour, EmploymentType, SpecialCondition,\
    Job, Essential, Desireable, JobCategory, JobSubCategory, JobSelectedCategory,\
    JobUploadDocumentType, JobUploadDocument

__author__ = 'ir4y'


class JobUploadDocumentTabInline(admin.TabularInline):
    model = JobUploadDocument


class EssentialTabInline(admin.TabularInline):
    model = Essential


class DesireableTabInline(admin.TabularInline):
    model = Desireable


class JobSelectedCategoryTabInline(admin.TabularInline):
    model = JobSelectedCategory


class JobAdmin(admin.ModelAdmin):
    inlines = (EssentialTabInline, DesireableTabInline, JobSelectedCategoryTabInline, JobUploadDocumentTabInline)

admin.site.register(Job, JobAdmin)
admin.site.register(JobLocation)
admin.site.register(JobArea)
admin.site.register(SalaryRange)
admin.site.register(Hour)
admin.site.register(EmploymentType)
admin.site.register(SpecialCondition)
admin.site.register(JobCategory)
admin.site.register(JobSubCategory)
admin.site.register(JobUploadDocumentType)

