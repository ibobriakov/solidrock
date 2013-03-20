from django.contrib.auth import authenticate, login
from tastypie import fields
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.resources import Resource
from main.api import ResourceLabelSchemaMixin, ResourceTypesOverrideSchemaMixin, ResourceFieldsOrderSchemaMixin
from ..models import AbstractUserObject, ActivationObject, LoginObject
from ..backends import RestBackend
from registration_rest_backend.api.resources import RegistrationResource
from registration_rest_backend.api.validation import RegisterValidation, LoginValidation
from userprofile.models import Employer, JobSeeker

__author__ = 'ir4y'


class EmployerRegistrationResource(RegistrationResource):
    user_type = fields.IntegerField(readonly=True, default=1)  # User.USER_TYPE_CHOICES 'Employer'
    company_name = fields.CharField(attribute='company_name')
    email_address = fields.CharField(attribute='email_address')
    phone_number = fields.CharField(attribute='phone_number')
    password = fields.CharField(attribute='password')
    re_password = fields.CharField(attribute='re_password')

    def create_profile(self, new_user, bundle):
        return Employer.objects.create(user=new_user,
                                       company=bundle.obj['company_name'],
                                       phone=bundle.obj['phone_number'])

    class Meta:
        resource_name = 'employer_registration'
        allowed_methods = ['post']
        object_class = AbstractUserObject
        always_return_data = True
        validation = RegisterValidation()
        fields_order = ('user_type', 'company_name', 'email_address', 'phone_number',
                        'password', 're_password', 'resource_uri')
        types_override = {
            'user_type': 'hidden',
            'email_address': 'email',
            'phone_number': 'phone',
            'password': 'password',
            're_password': 'password',
        }


class JobSeekerRegistrationResource(RegistrationResource):
    user_type = fields.IntegerField(readonly=True, default=0)  # User.USER_TYPE_CHOICES 'Job Seeker'
    first_name = fields.CharField(attribute='first_name')
    last_name = fields.CharField(attribute='last_name')
    email_address = fields.CharField(attribute='email_address')
    password = fields.CharField(attribute='password')
    re_password = fields.CharField(attribute='re_password')

    def create_profile(self, new_user, bundle):
        new_user.first_name = bundle.obj['first_name']
        new_user.last_name = bundle.obj['last_name']
        new_user.save()
        return JobSeeker.objects.create(user=new_user)

    class Meta:
        resource_name = 'job_seeker_registration'
        allowed_methods = ['post']
        object_class = AbstractUserObject
        always_return_data = True
        validation = RegisterValidation()
        fields_order = ('user_type', 'first_name', 'last_name', 'email_address',
                        'password', 're_password', 'resource_uri')
        types_override = {
            'user_type': 'hidden',
            'email_address': 'email',
            'password': 'password',
            're_password': 'password',
        }


class ActivationResource(Resource):
    """
    REST backend for user registration
    """
    activation_key = fields.CharField(attribute='activation_key')

    registration_backend = RestBackend()

    def obj_create(self, bundle, request=None, **kwargs):
        bundle = self.full_hydrate(bundle)
        self.registration_backend.activate(bundle.request, bundle.obj.activation_key)
        return bundle

    def get_schema(self, request, **kwargs):
        return self.create_response(request,  self.build_schema())

    def detail_uri_kwargs(self, bundle_or_obj):
        """
        Doesn't need this
        """
        return {}

    class Meta:
        resource_name = 'activation'
        allowed_methods = ['post']
        object_class = ActivationObject


class LoginResource(ResourceFieldsOrderSchemaMixin, ResourceLabelSchemaMixin,
                    ResourceTypesOverrideSchemaMixin, Resource):
    username = fields.CharField(attribute='username')
    password = fields.CharField(attribute='password')

    def get_schema(self, request, **kwargs):
        return self.create_response(request,  self.build_schema())

    def obj_create(self, bundle, request=None, **kwargs):
        self.is_valid(bundle)

        if bundle.errors:
            raise ImmediateHttpResponse(response=self.error_response(bundle.request, bundle.errors))

        bundle = self.full_hydrate(bundle)
        user = authenticate(username=bundle.obj.username, password=bundle.obj.password)
        if user is not None:
            login(bundle.request, user)
        return bundle

    def full_dehydrate(self, bundle, for_list=False):
        bundle.data = {'redirect_url': '/'}
        return bundle

    def detail_uri_kwargs(self, bundle_or_obj):
        """
        Doesn't need this
        """
        return {}

    class Meta:
        resource_name = 'login'
        allowed_methods = ['post']
        object_class = LoginObject
        always_return_data = True
        fields_order = ('username', 'password', 'resource_uri')
        validation = LoginValidation()
        types_override = {
            'password': 'password',
        }
