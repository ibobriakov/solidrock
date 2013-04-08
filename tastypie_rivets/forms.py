from django import forms
from django.core.urlresolvers import reverse
from django.forms.models import ModelChoiceIterator, ModelChoiceField, ChoiceField

__author__ = 'ir4y'





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


def ResourceSelect(resource_name=None, *args, **kwargs):
    return url_choice_field_fabric(get_api_url_fabric(resource_name))(*args,**kwargs)


def get_api_url_fabric(resource_name):
    return lambda obj: reverse('api_dispatch_detail', kwargs={'api_name': 'v1',
                                                              'resource_name': resource_name,
                                                              'pk': obj.pk})


def rivet_modelform_factory(base_name):
    class RivetModelForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(RivetModelForm, self).__init__(*args, **kwargs)
            for name, field in self.fields.iteritems():
                field.widget.attrs['data-value'] = base_name + "." + name
                setattr(field, 'type', base_name)
    return RivetModelForm