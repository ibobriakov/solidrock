from django import forms
from django.forms import HiddenInput
from django_select2 import Select2Widget
from models import ApplyToJob

__author__ = 'ir4y'


class ApplyToJobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApplyToJobForm, self).__init__(*args, **kwargs)
        self.fields['resume'].empty_label = ''
        self.fields['cover_letter'].empty_label = ''

    class Meta:
        model = ApplyToJob
        widgets = {
            'job': HiddenInput(),
            'resume': Select2Widget(select2_options={'placeholder': 'No Resume'}),
            'cover_letter': Select2Widget(select2_options={'placeholder': 'No Cover Letter'}),
        }
        exclude = ('job_seeker', )