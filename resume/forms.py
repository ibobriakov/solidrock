from django import forms
from django.core.urlresolvers import reverse
from django_select2 import Select2Widget
from models import Resume
from tastypie_rivets.forms.model import url_choice_field_fabric

__author__ = 'ir4y'


def get_url_fun(obj):
    return reverse('resume.edit', args=[obj.pk])


class ResumeSelectForm(forms.Form):
    resume = url_choice_field_fabric(get_url_fun)\
            (queryset=Resume.objects.none(),required=True, empty_label="",
             widget=Select2Widget(select2_options={'placeholder': 'Jump to Resume'}))