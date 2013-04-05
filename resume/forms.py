from django import forms
from django_select2 import Select2Widget
from dynamic_paper.forms import url_choice_field_fabric
from models import Resume

__author__ = 'ir4y'


class ResumeSelectForm(forms.Form):
    resume = url_choice_field_fabric('resume.edit')\
            (queryset=Resume.objects.none(),required=True, empty_label="",
             widget=Select2Widget(select2_options={'placeholder': 'Jump to Resume'}))