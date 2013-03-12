from tastypie import fields
from tastypie.resources import Resource

__author__ = 'ir4y'


class RegistrationResource(Resource):
    """
    REST backend for user registration
    """
    user_type = fields.CharField(attribute='user_type')
    company_name = fields.CharField(attribute='company_name')
    email_address = fields.CharField(attribute='email_address')
    phone_number = fields.CharField(attribute='phone_number')
    password = fields.CharField(attribute='password')
    re_password = fields.CharField(attribute='re_password')

    class Meta:
        resource_name = 'registration'
        allowed_methods = ['post']
