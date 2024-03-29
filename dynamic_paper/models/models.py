from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _


class PaperItemType(models.Model):
    name = models.CharField(verbose_name=_('Paper type name'), max_length=100)

    def is_list(self):
        return self.name.endswith("_list")

    def type_name(self):
        return self.name[:-5] if self.is_list() else self.name

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'dynamic_paper'


def paper_item_factory(*args, **kwargs):
    class _PaperItem(MPTTModel):
        paper = models.ForeignKey(*args, **kwargs)
        type = models.ForeignKey(PaperItemType, verbose_name=_('Type of element'))
        item_class = models.CharField(blank=True, null=True, max_length=50)
        placeholder = models.TextField(blank=True, null=True)
        value = models.TextField(verbose_name=_('Paper Item Value'), blank=True, null=True)
        parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

        def __unicode__(self):
            return "{value} [{type}]".format(value=self.value, type=self.type.__unicode__())

        def as_json(self):
            return {
                'id': self.id,
                'paper': self.paper_id,
                'item_class': self.item_class,
                'parent': self.parent_id if self.parent else False,
                'resource_uri': self.get_resource_uri(),
                'type': self.type.name,
                'value': self.value,
                'placeholder': self.placeholder,
                'children': [item.as_json() for item in self.get_children()]
            }

        class Meta:
            abstract = True
    return _PaperItem