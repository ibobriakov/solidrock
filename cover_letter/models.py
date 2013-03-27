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

    class Meta:
        app_label = 'cover_letter'


class  CoverLetterItem(paper_item_factory('cover_letter.CoverLetter', verbose_name=_('Cover Letter')), models.Model):
    def get_resource_uri(self):
        return reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'cover_letter', 'pk': self.pk})

    class Meta:
        app_label = 'cover_letter'


cover_letter_template = [
    lambda paper:CoverLetterItem(type=get_paper_item('right_list'), item_class="paper-right paper-block",
                                 value=" ", paper=paper),

    lambda paper:CoverLetterItem(type=get_paper_item('text'), item_class="title mini date", value="Date", paper=paper),

    lambda paper:CoverLetterItem(type=get_paper_item('text'), item_class="title mini", value="Re: Job Title",
                                 paper=paper),

    lambda paper:CoverLetterItem(type=get_paper_item('text'), item_class="paper-block", value="""Lorem ipsum dolor sit amet,
     consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat
     volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper.""", paper=paper),

    lambda paper:CoverLetterItem(type=get_paper_item('text'), item_class="paper-block", value="""Lorem ipsum dolor sit amet,
    consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat
    volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip
    ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat,
    vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent
    luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend
    option congue nihil imperdiet doming id quod mazim placerat facer possim assum.""", paper=paper),

    lambda paper:CoverLetterItem(type=get_paper_item('text'), item_class="paper-block", value="""Lorem ipsum dolor sit amet,
    consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
     Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea
     commodo consequat.""", paper=paper),

    lambda paper:CoverLetterItem(type=get_paper_item('text'), item_class="paper-block", value="Closing", paper=paper),

    lambda paper:CoverLetterItem(type=get_paper_item('text'), item_class="paper-block",
                                 value="Quick-reference contact number", paper=paper), ]

cover_letter_type_template = {
    'right': [
        lambda cover_letter_item:CoverLetterItem(type=get_paper_item('text'), item_class="paper-right", value="Name",
                                                 paper=cover_letter_item.paper, parent=cover_letter_item),

        lambda cover_letter_item:CoverLetterItem(type=get_paper_item('text'), item_class="paper-right", value="Address",
                                                 paper=cover_letter_item.paper, parent=cover_letter_item),

        lambda cover_letter_item:CoverLetterItem(type=get_paper_item('text'), item_class="paper-right", value="Phone Number",
                                                 paper=cover_letter_item.paper, parent=cover_letter_item),

        lambda cover_letter_item:CoverLetterItem(type=get_paper_item('text'), item_class="paper-right", value="Email Address",
                                                 paper=cover_letter_item.paper, parent=cover_letter_item),
    ]
}


def cover_letter_proxy(instance, created, **kwargs):
    return get_signal_for_page(cover_letter_template)(instance, created, **kwargs)


def cover_letter_item_proxy(instance, created, **kwargs):
    return get_signal_for_page_item(cover_letter_type_template)(instance, created, **kwargs)

post_save.connect(cover_letter_proxy, sender=CoverLetter)
post_save.connect(cover_letter_item_proxy, sender=CoverLetterItem)