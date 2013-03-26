from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.models import FlatPage
from flatblocks.forms import FlatBlockForm
from redactor.fields import RedactorEditor

__author__ = 'ir4y'


class WysiwygFlatpageForm(FlatpageForm):
    class Meta:
        model = FlatPage
        widgets = {'content': RedactorEditor}


class WysiwygFlatBlockForm(FlatBlockForm):
    class Meta:
        widgets = {'content': RedactorEditor}