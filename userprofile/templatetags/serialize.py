import json
from django.db.models.query import QuerySet
from utils import get_resource_class

__author__ = 'jackdevil'

from django import template

register = template.Library()


@register.filter()
def as_json(data):
    def tastypie_resource_serialize(data):
        data_resource = get_resource_class(type(data))
        bundle = data_resource.build_bundle(obj=data, request=None)
        bundle.request.path = "/"
        return data_resource.full_dehydrate(bundle).data
    return json.dumps(map(tastypie_resource_serialize, data if type(data) is QuerySet else [data]))

