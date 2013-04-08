from django import forms
from django.core.urlresolvers import reverse
from django_select2 import Select2Widget
from main.forms import url_choice_field_fabric
from models import CoverLetter

__author__ = 'ir4y'


def get_url_fun(cover_letter):
    return reverse('cover_letter.edit', args=[cover_letter.pk])

CoverLetterSelectField = url_choice_field_fabric(get_url_fun)


class CoverLetterSelectForm(forms.Form):
    cover_letter = CoverLetterSelectField(queryset=CoverLetter.objects.none(),required=True, empty_label="",
                                          widget=Select2Widget(select2_options={'placeholder': 'Jump to Cover Letter'}))