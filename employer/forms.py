from django_select2 import Select2Widget
from models import Job, Essential, Desireable
from tastypie_rivets import rivet_modelform_factory

__author__ = 'jackdevil'


class JobForm(rivet_modelform_factory('job')):
    class Meta:
        model = Job
        widgets = {'location': Select2Widget(select2_options={'placeholder': 'Select Location'}),
                   'area': Select2Widget(select2_options={'placeholder': 'Select Area'}),
                   'hours': Select2Widget(select2_options={'placeholder': 'Select Hour'}),
                   'employment_type': Select2Widget(select2_options={'placeholder': 'Select Type'}),
                   'special_conditions': Select2Widget(select2_options={'placeholder': 'Select Conditions'}),
                   }


class EssentialForm (rivet_modelform_factory('essential')):
    class Meta:
        model = Essential


class DesireableForm (rivet_modelform_factory('desireable')):
    class Meta:
        model = Desireable
