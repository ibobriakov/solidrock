from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from dynamic_paper.models import paper_item_factory


class CoverLetter(models.Model):
    name = models.CharField(verbose_name=_('Cover Letter Name'), max_length=100)
    owner = models.ForeignKey('auth.User')

    def __unicode__(self):
        return self.name


class  CoverLetterItem(paper_item_factory('cover_letter.CoverLetter', verbose_name=_('Cover Letter')),models.Model):
    def get_resource_uri(self):
        return reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'cover_letter', 'pk': self.pk})