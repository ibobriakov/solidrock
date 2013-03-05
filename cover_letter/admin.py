from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import CoverLetterItem, CoverLetter

__author__ = 'ir4y'


admin.site.register(CoverLetter)
admin.site.register(CoverLetterItem,MPTTModelAdmin)