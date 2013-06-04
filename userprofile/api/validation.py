from collections import defaultdict
from django.core.exceptions import ValidationError
from tastypie.validation import FormValidation
from main.api.validation import RequiredFiledValidationMixin
from django.core import validators

__author__ = 'ir4y'


class EmployerResourceValidation(RequiredFiledValidationMixin, FormValidation):
    def is_valid(self, bundle, request=None):
        errors = defaultdict(list)
        errors.update(super(EmployerResourceValidation, self).is_valid(bundle, request))
        if 'agree' not in bundle.data or bundle.data['agree'] != 'true':
            errors['agree'].append('You should accept user agreement')
        return errors


class JobSeekerInformationResourceValidation(RequiredFiledValidationMixin, FormValidation):
    def is_valid(self, bundle, request=None):
        errors = defaultdict(list)
        errors.update(super(JobSeekerInformationResourceValidation, self).is_valid(bundle, request))
        for field_name in ('first_name', 'last_name'):
            try:
                validators.MaxLengthValidator(30)(bundle.data[field_name])
            except ValidationError as err:
                errors[field_name].append(err.messages)
        return errors


