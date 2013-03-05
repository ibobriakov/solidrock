from django.db import models
from django.utils.translation import ugettext_lazy as _
from dynamic_paper.models import PaperItem


class CoverLetter(models.Model):
    name = models.CharField(verbose_name=_('Cover Letter Name'), max_length=100)
    owner = models.ForeignKey('auth.User')


class  CoverLetterItem(PaperItem):
    cover_letter = models.ForeignKey('cover_letter.CoverLetter', verbose_name=_('Resume'))

