from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import PaperItemType, PaperItem

__author__ = 'ir4y'

admin.site.register(PaperItemType)
admin.site.register(PaperItem, MPTTModelAdmin)