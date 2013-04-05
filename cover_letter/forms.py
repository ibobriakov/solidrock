from django import forms
from django_select2 import Select2Widget
from dynamic_paper.forms import url_choice_field_fabric
from models import CoverLetter

__author__ = 'ir4y'


class CoverLetterSelectForm(forms.Form):
    cover_letter = url_choice_field_fabric('cover_letter.edit')\
            (queryset=CoverLetter.objects.none(),required=True, empty_label="",
             widget=Select2Widget(select2_options={'placeholder': 'Jump to Cover Letter'}))