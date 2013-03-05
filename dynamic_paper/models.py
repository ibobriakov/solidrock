from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _


class PaperItemType(models.Model):
    name = models.CharField(verbose_name=_('Paper type name'), max_length=100)

    def __unicode__(self):
        return self.name


class PaperItem(MPTTModel):
    type = models.ForeignKey(PaperItemType, verbose_name=_('Type of element'))
    value = models.CharField(verbose_name=_('Paper Item Value'), max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return "{value} [{type}]".format(value=self.value,type=self.type.__unicode__())