from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from dynamic_paper.models import paper_item_factory
from dynamic_paper.models.signals import get_signal_for_page, get_signal_for_page_item
from dynamic_paper.utils import get_paper_item


class Resume(models.Model):
    name = models.CharField(verbose_name=_('Resume name'), max_length=100)
    owner = models.ForeignKey('auth.User')

    class Meta:
        app_label = 'resume'


class ResumeItem(paper_item_factory('resume.Resume', verbose_name=_('Resume'))):
    def get_resource_uri(self):
        return reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'resume', 'pk': self.pk})

    class Meta:
        app_label = 'resume'


resume_template = [
    lambda paper:ResumeItem(type=get_paper_item('text'), value="Your Name", paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('line'), value="", paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('text'), value="Your Address", paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('phone'), value="Your Phone", paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('text'), value="you@server.com", paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('header'), value="Career Overview", paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('list'), value="Key Strengths", paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('career'), value="Career History", paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('education'), value="Education & Training", paper=paper), ]

resume_items_template = {
    'phone': [
        lambda resume_item:ResumeItem(type=get_paper_item('text'), value="00 0000 0000",
                                      paper=resume_item.paper, parent=resume_item), ],
    'list': [
        lambda resume_item:ResumeItem(type=get_paper_item('text'), value="Lore ipsum",
                                      paper=resume_item.paper, parent=resume_item), ],
    'career': [
        lambda resume_item:ResumeItem(type=get_paper_item('date'), value="Month YYYY",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('date'), value="Month YYYY",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('text'), value="Job title",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('header'), value="Employer Company Name",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('list'), value="Key Responsibilities",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('list'), value="Key Achievements",
                                      paper=resume_item.paper, parent=resume_item), ],
    'education': [
        lambda resume_item:ResumeItem(type=get_paper_item('date'), value="YYYY",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('date'), value="YYYY",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('text'), value="School or University Name",
                                      paper=resume_item.paper, parent=resume_item), ]}


def resume_proxy(instance, created, **kwargs):
    return get_signal_for_page(resume_template)(instance, created, **kwargs)


def resume_item_proxy(instance, created, **kwargs):
    return get_signal_for_page_item(resume_items_template)(instance, created, **kwargs)

post_save.connect(resume_proxy, sender=Resume)
post_save.connect(resume_item_proxy, sender=ResumeItem)