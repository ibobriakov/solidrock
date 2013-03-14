from django.db import models
__author__ = 'ir4y'

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^userprofile\.models\.fields\.PhoneField"])


class PhoneField(models.CharField):
    max_length = 11
    default = '00000000000'

    def __init__(self, *args, **kwargs):
        if 'default' not in kwargs:
            kwargs['default'] = self.default
        if 'max_length' not in kwargs:
            kwargs['max_length'] = self.max_length
        super(PhoneField, self).__init__(*args, **kwargs)