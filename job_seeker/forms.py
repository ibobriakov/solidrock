from django.forms import HiddenInput
from django_select2 import Select2Widget
from models import ApplyToJob
from tastypie_rivets import rivet_modelform_factory

__author__ = 'ir4y'


class ApplyToJobForm(rivet_modelform_factory('apply_to_job')):
    class Meta:
        model = ApplyToJob
        widgets = {
            'job': HiddenInput(),
            'resume': Select2Widget(select2_options={'placeholder': 'No Resume'}),
            'cover_letter': Select2Widget(select2_options={'placeholder': 'No Cover Letter'}),
        }
        resource_names = {
            'cover_letter': 'cover_letter_name',
            'resume': 'resume_name'
        }
        exclude = ('job_seeker',)