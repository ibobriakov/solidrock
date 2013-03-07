from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from dynamic_paper.models import paper_item_factory
from dynamic_paper.models.signals import get_signal_for_page
from dynamic_paper.utils import get_paper_item


class CoverLetter(models.Model):
    name = models.CharField(verbose_name=_('Cover Letter Name'), max_length=100)
    owner = models.ForeignKey('auth.User')

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'cover_letter'


class  CoverLetterItem(paper_item_factory('cover_letter.CoverLetter', verbose_name=_('Cover Letter')), models.Model):
    def get_resource_uri(self):
        return reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'cover_letter', 'pk': self.pk})

    class Meta:
        app_label = 'cover_letter'


cover_letter_template = [
    lambda paper:CoverLetterItem(type=get_paper_item('text'), value="Name", paper=paper),
    lambda paper:CoverLetterItem(type=get_paper_item('text'), value="Address", paper=paper),
    lambda paper:CoverLetterItem(type=get_paper_item('text'), value="Phone Number", paper=paper),
    lambda paper:CoverLetterItem(type=get_paper_item('text'), value="Email Address", paper=paper),
    lambda paper:CoverLetterItem(type=get_paper_item('date'), value="Date", paper=paper),
    lambda paper:CoverLetterItem(type=get_paper_item('header'), value="Introduction", paper=paper),
    lambda paper:CoverLetterItem(type=get_paper_item('header'), value="Body", paper=paper),
    lambda paper:CoverLetterItem(type=get_paper_item('header'), value="Conclusion", paper=paper), ]


def cover_letter_proxy(instance, created, **kwargs):
    return get_signal_for_page(cover_letter_template)(instance, created, **kwargs)

post_save.connect(cover_letter_proxy, sender=CoverLetter)