from tastypie.resources import Resource
from main.api import ResourceTypesOverrideMixin
from tastypie.exceptions import BadRequest, ImmediateHttpResponse
from registration_rest_backend.backends import RestBackend

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
        self.is_valid(bundle)

        if bundle.errors:
            raise ImmediateHttpResponse(response=self.error_response(bundle.request, bundle.errors))
        bundle = self.full_hydrate(bundle)
        new_user = self.registration_backend.register(bundle.request,
                                                      username=bundle.obj['email_address'],
                                                      email=bundle.obj['email_address'],
                                                      password=bundle.obj['password'],
                                                      user_type=self.user_type.default)
        self.create_profile(new_user, bundle)
        return bundle

    def detail_uri_kwargs(self, bundle_or_obj):
        """
        Doesn't need this
        """
        return {}