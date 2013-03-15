from tastypie import fields
from tastypie.exceptions import BadRequest
from tastypie.resources import Resource
from main.api import ResourceTypesOverrideMixin
from models import AbstractUserObject, ActivationObject
from backends import RestBackend
from userprofile.models import Employer, JobSeeker

__author__ = 'ir4y'


class RegistrationResource(ResourceTypesOverrideMixin, Resource):
    """
    REST backend for user registration
    """
    USER_TYPE_CHOICES = (
        (0, 'Job Seeker'),
        (1, 'Employer'),
    )
    registration_backend = RestBackend()

    def full_dehydrate(self, bundle, for_list=False):
        del(bundle.data['password'])
        del(bundle.data['re_password'])
        bundle.data['redirect_url'] = '/'
        return bundle

    def get_schema(self, request, **kwargs):
        return self.create_response(request,  self.build_schema())

    def obj_create(self, bundle, request=None, **kwargs):
        if not bundle.request.user.is_anonymous():
            raise BadRequest("You shouldn't be authorized")
        bundle = self.full_hydrate(bundle)

        if bundle.obj['password'] != bundle.obj['re_password']:
            raise BadRequest('Password missmatch')

        new_user = self.registration_backend.register(bundle.request,
                                                      username=bundle.obj['email_address'],
                                                      email=bundle.obj['email_address'],
                                                      password=bundle.obj['password'],
                                                      user_type=self.user_type)
        self.create_profile(new_user, bundle)
        return bundle

    def detail_uri_kwargs(self, bundle_or_obj):
        """
        Doesn't need this
        """
        return {}


class EmployerRegistrationResource(RegistrationResource):
    user_type = 1  # User.USER_TYPE_CHOICES 'Employer'
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
        types_override = {
            'password': 'password',
            're_password': 'password',
            'email_address': 'email',
            'phone_number': 'phone',
        }


class JobSeekerRegistrationResource(RegistrationResource):
    user_type = 0  # User.USER_TYPE_CHOICES 'Job Seeker'
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
        resource_name = 'jobseeker_registration'
        allowed_methods = ['post']
        object_class = AbstractUserObject
        always_return_data = True
        types_override = {
            'password': 'password',
            're_password': 'password',
            'email_address': 'email',
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

    def detail_uri_kwargs(self, bundle_or_obj):
        """
        Doesn't need this
        """
        return {}

    class Meta:
        resource_name = 'activation'
        allowed_methods = ['post']
        object_class = ActivationObject