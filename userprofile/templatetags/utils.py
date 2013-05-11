from django.conf import settings
from django.utils.importlib import import_module


__author__ = 'ir4y'


def get_resource_class(model_class):
    for app in settings.INSTALLED_APPS:
        try:
            resource_api = import_module('%s.api' % app)
            for resource_klass_name in resource_api.__all__:
                resource_klass = getattr(resource_api, resource_klass_name)()
                if resource_klass._meta.queryset.model == model_class:
                    return resource_klass
        except:
            continue
    return None
