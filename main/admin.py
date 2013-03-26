from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from flatblocks.admin import FlatBlockAdmin
from flatblocks.models import FlatBlock
from forms import WysiwygFlatpageForm, WysiwygFlatBlockForm

__author__ = 'ir4y'

admin.site.unregister(FlatPage)
admin.site.unregister(FlatBlock)


class WysiwygFlatPageAdmin(FlatPageAdmin):
    form = WysiwygFlatpageForm


class WysiwygFlatBlockAdmin(FlatBlockAdmin):
    form = WysiwygFlatBlockForm


admin.site.register(FlatPage, WysiwygFlatPageAdmin)
admin.site.register(FlatBlock, WysiwygFlatBlockAdmin)
