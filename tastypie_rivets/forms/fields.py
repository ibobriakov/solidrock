from tastypie_rivets.forms.model import url_choice_field_fabric
from tastypie_rivets.utils import get_api_url_fabric

__author__ = 'ir4y'


def ResourceSelect(resource_name=None, *args, **kwargs):
    return url_choice_field_fabric(get_api_url_fabric(resource_name))(*args, **kwargs)