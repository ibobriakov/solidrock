from django import template

__author__ = 'ir4y'


register = template.Library()


def startswith(string, startswith):
    return string.startswith(startswith)

register.filter('startswith', startswith)
