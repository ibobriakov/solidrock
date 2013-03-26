from tastypie.validation import FormValidation

__author__ = 'ir4y'


class EmployerResourceValidation(FormValidation):
    def is_valid(self, bundle, request=None):
        errors = super(EmployerResourceValidation, self).is_valid(bundle, request)
        if 'agree' not in bundle.data or not bundle.data['agree']:
            errors['agree'] = 'You should accept user agreement'
        return errors
