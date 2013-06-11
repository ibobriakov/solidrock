from collections import defaultdict
from tastypie.validation import FormValidation


__author__ = 'ir4y'


class RequiredFiledValidationMixin(object):
    """
    REQUIRED_FIELDS dog-nail
    It's made for preload feature
    """
    def is_valid(self, bundle, request=None):
        errors = defaultdict(list)
        errors.update(super(RequiredFiledValidationMixin, self).is_valid(bundle, request))
        for key, value in bundle.data.items():
            if key in self.form_class._meta.model.REQUIRED_FIELDS and not value:
                fields = self.form_class().fields
                if key in fields and fields[key].required:
                    continue
                errors[key].append('This field is required.')
        return errors


class FormWithRequiredFiledValidation(RequiredFiledValidationMixin, FormValidation):
    pass