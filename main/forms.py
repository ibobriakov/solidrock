from django import forms
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


def rivet_modelform_factory(base_name):
    class RivetModelForm(forms.ModelForm):
        def __init__(self, *agrs, **kwargs):
            super(RivetModelForm, self).__init__(*agrs, **kwargs)
            for name, field in self.fields.iteritems():
                field.widget.attrs['data-value'] = base_name + "." + name
    return RivetModelForm