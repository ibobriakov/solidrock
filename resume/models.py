# -*- coding: utf8 -*-
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

    def __unicode__(self):
        return self.name

    @property
    def list_set(self):
        return self.resumeitem_set

    class Meta:
        app_label = 'resume'


class ResumeItem(paper_item_factory('resume.Resume', verbose_name=_('Resume'))):
    def get_resource_uri(self):
        return reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'resume', 'pk': self.pk})

    class Meta:
        app_label = 'resume'

resume_template = [
    lambda paper:ResumeItem(type=get_paper_item('text'), item_class="title oneline", placeholder="Your Name",
                            paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('line'), item_class="line_break", value=" ",
                            paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('text'), item_class="oneline", placeholder="Your Address",
                            paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('phone_list'), item_class="title mini relativity", value="Phones",
                            paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('header'), item_class="title mini span", value="Email",
                            paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('text'), item_class="span oneline", placeholder="you@server.com",
                            paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('header'), item_class="title", value="Career Overview",
                            paper=paper),

    lambda paper:ResumeItem(type=get_paper_item('text'), item_class="multiline", placeholder="""Lorem ipsum dolor sit amet,
    consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat
    volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut
    aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse
    molestie consequat.""", paper=paper),

    lambda paper:ResumeItem(type=get_paper_item('keystrengts_list'), item_class="title relativity", value="Key Strengths",
                            paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('career_list'), item_class="title relativity", value="Career History",
                            paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('education_list'), item_class="title relativity", value="Education & Training",
                            paper=paper),
    lambda paper:ResumeItem(type=get_paper_item('personal_list'), item_class="title relativity", value="Personal Memberships",
                            paper=paper), ]

resume_type_template = {
    'phone': [
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="title mini span oneline",
                                      placeholder="Phone Type", paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="span oneline", placeholder="00 0000 0000",
                                      paper=resume_item.paper, parent=resume_item), ],

    'keystrengts': [
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="list-item span oneline",
                                      placeholder="Lore Ipsum", paper=resume_item.paper, parent=resume_item), ],

    'career': [
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="title mini span oneline", placeholder="MM YYYY",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="title mini span oneline", placeholder="MM YYYY",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('line'), item_class="span", value="|",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="title mini span oneline",
                                      placeholder="Job title", paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="title wide oneline",
                                      placeholder="Employer Company Name", paper=resume_item.paper, parent=resume_item),

        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="multiline", placeholder="""Lorem ipsum dolor sit amet,
        consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat
        volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut
        aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse
        molestie consequat.""", paper=resume_item.paper, parent=resume_item),

        lambda resume_item:ResumeItem(type=get_paper_item('keyresponsibilities_list'), item_class="title mini relativity",
                                      value="Key Responsibilities",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('keyachievements_list'), item_class="title mini relativity",
                                      value="Key Achievements",
                                      paper=resume_item.paper, parent=resume_item), ],
    'keyachievements': [
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="list-item span oneline",
                                      placeholder="Lore Ipsum", paper=resume_item.paper, parent=resume_item), ],
    'keyresponsibilities': [
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="list-item span oneline",
                                      placeholder="Lore Ipsum", paper=resume_item.paper, parent=resume_item), ],
    'education': [
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="title span oneline", placeholder="YYYY",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('line'), item_class="title span", value="-",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="title span oneline", placeholder="YYYY",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('line'), item_class="title span", value="|",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('text'), placeholder="School or University Name",
                                      paper=resume_item.paper, item_class="title span oneline", parent=resume_item), ],
    'personal': [
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="title mini span oneline",
                                      placeholder="Organization", paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="span oneline", placeholder="MM YYYY",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('line'), item_class="span", value="-",
                                      paper=resume_item.paper, parent=resume_item),
        lambda resume_item:ResumeItem(type=get_paper_item('text'), item_class="span oneline", placeholder="MM YYYY",
                                      paper=resume_item.paper, parent=resume_item), ]}

# Структура данных для резюме:
# В списке resume_template находятся элементы верхнего уровня
# Если они являются списком, то их тип заканчивается на '_list'
# Если тип сложный, то он описывается в словаре resume_type_template
# Простые типы:
# text - редактируемый с помощью input текст
# date - редактируемое поле даты
# line - просто линия не редактируемая
# header - нередактируемый заголовок
# Сложный тип состоит из нескольких простых (как структура)

# Поведение резюме:
# При добавлении элемента типа container со значнием являющимся типом (простым или сложным)
# Для него автоматически создается внутренняя иерархия элементов для которой он будет являться родителем.


def resume_proxy(instance, created, **kwargs):
    return get_signal_for_page(resume_template)(instance, created, **kwargs)


def resume_item_proxy(instance, created, **kwargs):
    return get_signal_for_page_item(resume_type_template)(instance, created, **kwargs)

post_save.connect(resume_proxy, sender=Resume)
post_save.connect(resume_item_proxy, sender=ResumeItem)