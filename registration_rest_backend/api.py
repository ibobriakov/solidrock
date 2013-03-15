from tastypie import fields
from tastypie.exceptions import BadRequest
from tastypie.resources import Resource
from models import AbstractUserObject, ActivationObject
from backends import RestBackend
from userprofile.models import Employer, JobSeeker

__author__ = 'ir4y'


class RegistrationResource(Resource):
    """
    REST backend for user registration
    """
    user_type = fields.CharField(attribute='user_type')
    company_name = fields.CharField(attribute='company_name')
    first_name = fields.CharField(attribute='first_name')
    last_name = fields.CharField(attribute='last_name')
    email_address = fields.CharField(attribute='email_address')
    phone_number = fields.CharField(attribute='phone_number')
    password = fields.CharField(attribute='password')
    re_password = fields.CharField(attribute='re_password')

    registration_backend = RestBackend()

    def obj_create(self, bundle, request=None, **kwargs):
        if not bundle.request.user.is_anonymous():
            raise BadRequest("You shouldn't be authorized")
        bundle = self.full_hydrate(bundle)

        if bundle.obj['password'] != bundle.obj['re_password']:
            raise BadRequest('Password missmatch')

        if bundle.obj['user_type'] in ('employer', 'job_seeker'):
            new_user = self.registration_backend.register(bundle.request,
                                                          username=bundle.obj['email_address'],
                                                          email=bundle.obj['email_address'],
                                                          password=bundle.obj['password'],)
            if bundle.obj['user_type'] == 'employer':
                Employer.objects.create(user=new_user,
                                        company=bundle.obj['company_name'],
                                        phone=bundle.obj['phone_number'])
                new_user.user_type = 1  # User.USER_TYPE_CHOICES 'Employer'
            elif bundle.obj['user_type'] == 'job_seeker':
                JobSeeker.objects.create(user=new_user)
                new_user.first_name = bundle.obj['first_name']
                new_user.last_name = bundle.obj['last_name']
                new_user.user_type = 0  # User.USER_TYPE_CHOICES 'Job Seeker'
            new_user.save()
        else:
            raise BadRequest('Bad user type')
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
        always_return_data = True


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
