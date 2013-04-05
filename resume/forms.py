from django import forms
from django_select2 import Select2Widget
from models import Resume

__author__ = 'ir4y'


class ResumeSelectForm(forms.Form):
    resume = forms.ModelChoiceField(queryset=Resume.objects.none(),required=True,
                                    widget=Select2Widget(select2_options={'placeholder': 'Jump to Resume'}))