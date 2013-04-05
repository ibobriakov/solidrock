from django.core.urlresolvers import reverse
from django.forms.fields import ChoiceField
from django.forms.models import ModelChoiceIterator, ModelChoiceField

__author__ = 'ir4y'


def url_choice_field_fabric(model_edit_view):
    class UrlModelChoiceIterator(ModelChoiceIterator):
        def choice(self, obj):
            url = reverse(model_edit_view, args=[obj.pk])
            return (url, self.field.label_from_instance(obj))

    class UrlModelChoiceField(ModelChoiceField):
        def _get_choices(self):
            if hasattr(self, '_choices'):
                return self._choices
            return UrlModelChoiceIterator(self)
        choices = property(_get_choices, ChoiceField._set_choices)

    return UrlModelChoiceField
