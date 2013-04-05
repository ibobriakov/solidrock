from collections import defaultdict
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from tastypie.validation import Validation
from userprofile.models import Employer


class RegisterValidation(Validation):
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'Not quite what I had in mind.'}

        errors = defaultdict(list)

        if not bundle.request.user.is_anonymous():
            errors['__all__'].append('You should not be login for register')
        if bundle.data['password'] != bundle.data['re_password']:
            errors["password"].append('Password missmatch')

        for key, value in bundle.data.items():
            if not value:
                errors[key].append('Field required')
        try:
            validate_email(bundle.data['email_address'])
        except ValidationError as err:
            errors['email_address'].append(err.messages)

        if User.objects.filter(email=bundle.data['email_address']).count():
            errors['email_address'].append("User with this email is already exists")

        if 'company_name' in bundle.data:
            if Employer.objects.filter(company=bundle.data['company_name']).count():
                errors['company_name'].append("Employer with this company name already exists")

        if 'phone_number' in bundle.data:
            if len(bundle.data['phone_number']) > 11:
                errors['phone_number'].append("Phone number is too long")

        return errors


class LoginValidation(Validation):
    def is_valid(self, bundle, request=None):
        errors = defaultdict(list)
        username = bundle.data['username']
        password = bundle.data['password']
        for key, value in bundle.data.items():
            if not value:
                errors[key].append('Field required')
        user = authenticate(email=username, password=password)
        if user is None:
            errors['username'].append("User password miss match")
        return errors