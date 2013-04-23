from tastypie.resources import ModelResource
from cover_letter import api as cover_letter_api
from registration_rest_backend import api as registration_rest_backend_api
from resume import api as resume_api
from userprofile import api as userprofile_api
from employer import api as employer_api
from payment import api as payment_api

__author__ = 'ir4y'


def get_resource_class(model_class):
    api_list = []

    def get_import_list(module):
        modules = []
        for item in module.__all__:
            resource = getattr(module, item)()
            if isinstance(resource, ModelResource):
                modules.append(resource)
        return modules

    for item in map(get_import_list, [cover_letter_api, registration_rest_backend_api, resume_api,
                                      userprofile_api, employer_api, payment_api]):
        api_list.extend(item)
    return {resource._meta.queryset.model: resource for resource in api_list}[model_class]
