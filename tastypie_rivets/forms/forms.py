from django import forms
from django.forms.models import ModelChoiceField
from tastypie_rivets.forms.fields import ResourceSelect

__author__ = 'ir4y'


def rivet_modelform_factory(base_name):
    class RivetModelForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(RivetModelForm, self).__init__(*args, **kwargs)
            for name, field in self.fields.iteritems():
                field.widget.attrs['data-value'] = base_name + "." + name
                setattr(field, 'type', base_name)
                if isinstance(field, ModelChoiceField):
                    required = field.required | (name in getattr(self.Meta.model, 'REQUIRED_FIELDS', []))
                    # REQUIRED_FIELDS dog-nail see employer/models.py:54: %-)
                    resource_name_map = getattr(self.Meta, 'resource_names', {})
                    kwargs = {'resource_name':  resource_name_map.get(name,field.queryset.model.__name__.lower()),
                              'queryset': field.queryset,
                              'empty_label': '',
                              'required': required}
                    widgets = getattr(self.Meta, 'widgets', {})
                    if name in widgets:
                        kwargs['widget'] = widgets[name]
                    self.fields[name] = ResourceSelect(**kwargs)
    return RivetModelForm