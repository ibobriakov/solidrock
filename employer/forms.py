__author__ = 'jackdevil'

from django_select2 import Select2Widget
from tastypie_rivets import rivet_modelform_factory
from employer.models import Job


class JobForm(rivet_modelform_factory('job')):
    class Meta:
        model = Job
        # widgets = {
        #     'location': Select2Widget(select2_options={'placeholder': 'Select Location'}),
        #     'area': Select2Widget(select2_options={'placeholder': 'Select Area'}),
        #     'hours': Select2Widget(select2_options={'placeholder': 'Select Hour'}),
        #     'employment_type': Select2Widget(select2_options={'placeholder': 'Select Type'}),
        #     'special_conditions': Select2Widget(select2_options={'placeholder': 'Select Conditions'}),
        # }