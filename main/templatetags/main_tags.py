import re
from django import template
from django.utils.safestring import mark_safe

__author__ = 'ir4y'


register = template.Library()


@register.filter()
def startswith(string, startswith):
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
def if_value(value, else_value):
    return value if value else else_value
