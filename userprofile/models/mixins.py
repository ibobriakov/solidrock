from django.db import models
from django.utils.text import slugify
from userprofile.models.utils import create_model
from django.utils.translation import ugettext_lazy as _

__author__ = 'ir4y'


class AddressMixin(models.Model):
    address_first = models.CharField(max_length=255, blank=True, null=True)
    address_second = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True


def SlugTraits(base_filed_name='name', verbose_name=_("slug")):
    fileld_name = base_filed_name + '_slug'
    fields = {
        fileld_name: models.SlugField(verbose_name=verbose_name, max_length=255, blank=True, null=True)
    }
    SlugMixin = create_model('SlugMixin', fields=fields, module='main.models', options={'abstract': True})

    def save(self, **kwargs):
        original_text = getattr(self, base_filed_name)
        slug_text = slugify(original_text)
        setattr(self, fileld_name, slug_text)
        return super(SlugMixin, self).save(**kwargs)
    setattr(SlugMixin, 'save', save)
    return SlugMixin