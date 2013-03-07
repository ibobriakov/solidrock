from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import ResumeItem, Resume


__author__ = 'ir4y'


class ResumeItemInline(admin.TabularInline):
    model = ResumeItem


class ResumeAdmin(admin.ModelAdmin):
    inlines = [ResumeItemInline, ]

admin.site.register(Resume, ResumeAdmin)
admin.site.register(ResumeItem, MPTTModelAdmin)