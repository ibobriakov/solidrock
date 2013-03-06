from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import CoverLetterItem, CoverLetter

__author__ = 'ir4y'


class CoverLetterItemInline(admin.TabularInline):
    model = CoverLetterItem


class CoverLetterAdmin(admin.ModelAdmin):
    inlines = [CoverLetterItemInline, ]

admin.site.register(CoverLetter, CoverLetterAdmin)
admin.site.register(CoverLetterItem, MPTTModelAdmin)