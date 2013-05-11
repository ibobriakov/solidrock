from django import forms
from django.forms.models import ModelChoiceField
from tastypie_rivets.forms.fields import ResourceSelect

__author__ = 'ir4y'


def rivet_modelform_factory(base_name):
    class RivetModelForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(RivetModelForm, self).__init__(*args, **kwargs)
            for name, field in self.fields.iteritems():
                if isinstance(field, ModelChoiceField):
                    required = field.required | (name in getattr(self.Meta.model, 'REQUIRED_FIELDS', []))
                    # REQUIRED_FIELDS dog-nail see employer/models.py:54: %-)
                    widgets = getattr(self.Meta, 'widgets', {})
                    resource_map = getattr(self.Meta, 'resource_names', {})
                    kwargs = {'resource_name': resource_map[name] if name in resource_map else field.queryset.model.__name__.lower(),
                              'queryset': field.queryset,
                              'empty_label': '',
                              'required': required}
                    if name in widgets:
                        kwargs['widget'] = widgets[name]
                    self.fields[name] = ResourceSelect(**kwargs)
                    self.fields[name].widget.attrs['ui-select2'] = '{allowClear:true}'
                    self.fields[name].widget.attrs['data-placeholder'] = 'Select item'
                self.fields[name].widget.attrs['ng-model'] = base_name + "." + name
    return RivetModelForm