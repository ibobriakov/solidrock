from django.db import models
__author__ = 'ir4y'


class PhoneField(models.CharField):
    max_length = 11
    default = '00000000000'