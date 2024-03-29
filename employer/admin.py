from django.contrib import admin
from models import JobLocation, JobArea,  Hour, EmploymentType, SpecialCondition,\
    Job, Essential, Desireable, JobCategory, JobSubCategory, JobSelectedCategory,\
    JobUploadDocumentType, JobUploadDocument, JobExecutivePositions, JobSelectedSubCategory

__author__ = 'ir4y'


class JobUploadDocumentTabInline(admin.TabularInline):
    model = JobUploadDocument


class EssentialTabInline(admin.TabularInline):
    model = Essential


class DesireableTabInline(admin.TabularInline):
    model = Desireable


class JobSelectedCategoryTabInline(admin.TabularInline):
    model = JobSelectedCategory


class JobSelectedSubCategoryTabInline(admin.TabularInline):
    model = JobSelectedSubCategory


class JobAdmin(admin.ModelAdmin):
    inlines = (EssentialTabInline, DesireableTabInline,
               JobSelectedCategoryTabInline, JobSelectedSubCategoryTabInline, JobUploadDocumentTabInline)

admin.site.register(Job, JobAdmin)
admin.site.register(JobLocation)
admin.site.register(JobArea)
admin.site.register(Hour)
admin.site.register(EmploymentType)
admin.site.register(SpecialCondition)
admin.site.register(JobCategory)
admin.site.register(JobSubCategory)
admin.site.register(JobUploadDocumentType)
admin.site.register(JobExecutivePositions)

