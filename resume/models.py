from django.db import models
from django.utils.translation import ugettext_lazy as _
from dynamic_paper.models import PaperItem


class Resume(models.Model):
    name = models.CharField(verbose_name=_('Resume name'), max_length=100)
    owner = models.ForeignKey('auth.User')


class ResumeItem(PaperItem):
    resume = models.ForeignKey('resume.Resume', verbose_name=_('Resume'))

