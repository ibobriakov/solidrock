from django.db import models

__author__ = 'ir4y'


class AddressMixin(models.Model):
    address_first = models.CharField(max_length=255, blank=True)
    address_second = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(verbose_name='Postcode', max_length=10, blank=True)

    class Meta:
        abstract = True
