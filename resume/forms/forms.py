from django import forms
from django_select2 import Select2Widget
from ..models import Resume
from options import UrlModelChoiceField

__author__ = 'ir4y'



class ResumeSelectForm(forms.Form):
    resume = UrlModelChoiceField(queryset=Resume.objects.none(),required=True, empty_label="",
                                    widget=Select2Widget(select2_options={'placeholder': 'Jump to Resume'}))