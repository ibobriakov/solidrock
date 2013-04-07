from django import forms
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.models import FlatPage
from django.forms.fields import ChoiceField
from django.forms.models import ModelChoiceIterator, ModelChoiceField
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
                setattr(field, 'type', base_name)
    return RivetModelForm


def url_choice_field_fabric(get_url_fun):
    class UrlModelChoiceIterator(ModelChoiceIterator):
        def choice(self, obj):
            url = get_url_fun(obj)
            return (url, self.field.label_from_instance(obj))

    class UrlModelChoiceField(ModelChoiceField):
        def _get_choices(self):
            if hasattr(self, '_choices'):
                return self._choices
            return UrlModelChoiceIterator(self)
        choices = property(_get_choices, ChoiceField._set_choices)

    return UrlModelChoiceField