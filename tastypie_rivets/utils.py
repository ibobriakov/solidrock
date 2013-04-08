from django.core.urlresolvers import reverse

__author__ = 'ir4y'


def get_api_url_fabric(resource_name):
    #todo set api_name as agrument for rivet_modelform_factory
    return lambda obj: reverse('api_dispatch_detail', kwargs={'api_name': 'v1',
                                                              'resource_name': resource_name,
                                                              'pk': obj.pk})