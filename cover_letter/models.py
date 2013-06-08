from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from dynamic_paper.models import paper_item_factory
from dynamic_paper.models.signals import get_signal_for_page, get_signal_for_page_item
from dynamic_paper.utils import get_paper_item


class CoverLetter(models.Model):
    name = models.CharField(verbose_name=_('Cover Letter Name'), max_length=100)
    owner = models.ForeignKey('auth.User')

    def __unicode__(self):
        return self.name

    @property
    def list_set(self):
        return self.coverletteritem_set

    class Meta:
        app_label = 'cover_letter'


class CoverLetterItem(paper_item_factory('cover_letter.CoverLetter', verbose_name=_('Cover Letter')), models.Model):
    def get_resource_uri(self):
        return reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'cover_letter', 'pk': self.pk})

    class Meta:
        app_label = 'cover_letter'


cover_letter_template = [

    lambda paper: CoverLetterItem(type=get_paper_item('text'), item_class="paper-right", placeholder="Name",
                                  paper=paper),

    lambda paper: CoverLetterItem(type=get_paper_item('text'), item_class="paper-right", placeholder="Address",
                                  paper=paper),

    lambda paper: CoverLetterItem(type=get_paper_item('text'), item_class="paper-right", placeholder="Phone Number",
                                  paper=paper),

    lambda paper: CoverLetterItem(type=get_paper_item('text'), item_class="paper-right", placeholder="Email Address",
                                  paper=paper),

    lambda paper: CoverLetterItem(type=get_paper_item('text'), item_class="title mini date clear", placeholder="Date",
                                  paper=paper),

    lambda paper: CoverLetterItem(type=get_paper_item('text'), item_class="title mini clear",
                                  placeholder="Re: Job Title",
                                  paper=paper),

    lambda paper: CoverLetterItem(type=get_paper_item('blocks_list'), item_class="paper-right paper-block",
                                  value=" ", paper=paper),

    lambda paper: CoverLetterItem(type=get_paper_item('text'), item_class="paper-block", placeholder="Closing",
                                  paper=paper),

    lambda paper: CoverLetterItem(type=get_paper_item('text'), item_class="paper-block",
                                  placeholder="Quick-reference contact number", paper=paper), ]

cover_letter_type_template = {
    'blocks': [
        lambda cover_letter_item: CoverLetterItem(type=get_paper_item('text'), item_class="paper-block multiline",
                                                  placeholder="""Lorem ipsum dolor sit amet,
     consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat
     volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper.""", paper=cover_letter_item.paper,
                                                  parent=cover_letter_item),
    ]
}


def cover_letter_proxy(instance, created, **kwargs):
    return get_signal_for_page(cover_letter_template)(instance, created, **kwargs)


def cover_letter_item_proxy(instance, created, **kwargs):
    return get_signal_for_page_item(cover_letter_type_template)(instance, created, **kwargs)


post_save.connect(cover_letter_proxy, sender=CoverLetter)
post_save.connect(cover_letter_item_proxy, sender=CoverLetterItem)