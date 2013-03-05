from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import ResumeItem, Resume

__author__ = 'ir4y'


admin.site.register(Resume)
admin.site.register(ResumeItem,MPTTModelAdmin)