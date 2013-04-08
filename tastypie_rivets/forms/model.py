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