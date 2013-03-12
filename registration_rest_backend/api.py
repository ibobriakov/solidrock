from tastypie import fields
from tastypie.bundle import Bundle
from tastypie.resources import Resource
from models import AbstractUserObject, ActivationObject

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

    def obj_create(self, bundle, request=None, **kwargs):
        bundle = self.full_hydrate(bundle)
        #todo add user registration
        return bundle

    def detail_uri_kwargs(self, bundle_or_obj):
        """
        Doesn't need this
        """
        return {}

    class Meta:
        resource_name = 'registration'
        allowed_methods = ['post']
        object_class = AbstractUserObject


class ActivationResource(Resource):
    """
    REST backend for user registration
    """
    activation_key = fields.CharField(attribute='activation_key')

    def obj_create(self, bundle, request=None, **kwargs):
        bundle = self.full_hydrate(bundle)
        #todo add user activation
        return bundle

    def detail_uri_kwargs(self, bundle_or_obj):
        """
        Doesn't need this
        """
        return {}

    class Meta:
        resource_name = 'activation'
        allowed_methods = ['post']
        object_class = ActivationObject
