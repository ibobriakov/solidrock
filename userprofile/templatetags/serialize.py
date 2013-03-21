import json
from django.db.models.query import QuerySet

__author__ = 'jackdevil'

from django import template

register = template.Library()


@register.filter(name='as_json')
def as_json(data):
    if type(data) is QuerySet:
        return json.dumps([model.as_dict() for model in data])
    else:
        return json.dumps([data.as_dict()])
