from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from tastypie.validation import Validation


class RegisterValidation(Validation):
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'Not quite what I had in mind.'}

        errors = {}

        if not bundle.request.user.is_anonymous():
            errors['__all__'] = ['You should not be login for register.']
        if bundle.data['password'] != bundle.data['re_password']:
            errors["password"] = ['password missmatch']

        for key, value in bundle.data.items():
            if not value:
                if key not in errors:
                    errors[key] = []
                errors[key].append('required.')
        try:
            validate_email(bundle.data['email_address'])
        except ValidationError as err:
            if 'email_address' not in errors:
                errors['email_address'] = []
            errors['email_address'] = err

        return errors