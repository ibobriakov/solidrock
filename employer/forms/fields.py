from main.forms import url_choice_field_fabric
from main.utils import get_api_url_fabric

__author__ = 'ir4y'


def ResourceSelect(resource_name=None, *args, **kwargs):
    return url_choice_field_fabric(get_api_url_fabric(resource_name))(*args,**kwargs)