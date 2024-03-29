import copy
import json
import re
from django import template
from django.utils.safestring import mark_safe

__author__ = 'ir4y'


register = template.Library()


@register.filter()
def as_title(string):
    title = copy.copy(string)
    if '.' in title:
        title = title.split('.')[0]
    return " ".join(map(lambda u: u.capitalize(), title.split('_')))


@register.filter()
def startswith(string, startswith):
    if string:
        return string.startswith(startswith)


@register.filter()
def is_job_seeker(user):
    return not user.user_type


@register.filter()
def is_employer(user):
    return user.user_type

class_re = re.compile(r'(?<=class=["\'])(.*)(?=["\'])')


@register.filter
def add_class(value, css_class):
    string = unicode(value)
    match = class_re.search(string)
    if match:
        m = re.search(r'^%s$|^%s\s|\s%s\s|\s%s$' % (css_class, css_class,
                                                    css_class, css_class), match.group(1))
        print match.group(1)
        if not m:
            return mark_safe(class_re.sub(match.group(1) + " " + css_class,
                                          string))
    else:
        return mark_safe(string.replace('>', ' class="%s">' % css_class))
    return value


@register.filter
def contain_list(value):
    return True if len(str(value).split('_'))>1 and str(value).split('_')[1] == 'list' else False


@register.simple_tag
def paper_tree(paper):
    return json.dumps([item.as_json() for item in paper.list_set.filter(parent=None)])


@register.filter
def is_span(node):
    return "span" in node.item_class


@register.filter
def is_li(node):
    return "list-item" in node.item_class


@register.filter
def is_ul(node):
    return node.value in ("Key Strengths", "Key Responsibilities", "Key Achievements",)

