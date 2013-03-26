from django import template

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
