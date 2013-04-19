from django import forms
from django.core.urlresolvers import reverse
from django_select2 import Select2Widget
from models import CoverLetter
from tastypie_rivets.forms.model import url_choice_field_fabric

__author__ = 'ir4y'


def get_url_fun(obj):
    return reverse('cover_letter.edit', args=[obj.pk])


class CoverLetterSelectForm(forms.Form):
    cover_letter = url_choice_field_fabric(get_url_fun)\
            (queryset=CoverLetter.objects.none(),required=True, empty_label="",
             widget=Select2Widget(select2_options={'placeholder': 'Jump to Cover Letter'}))