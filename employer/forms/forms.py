from django_select2 import Select2Widget
from main.forms import rivet_modelform_factory
from ..models import Job, JobLocation, Hour, EmploymentType, SpecialCondition, JobArea
from fields import ResourceSelect
__author__ = 'jackdevil'


class JobForm(rivet_modelform_factory('job')):
    location = ResourceSelect(resource_name='joblocation', queryset=JobLocation.objects.all(), required=True,
                              empty_label="", widget=Select2Widget(select2_options={'placeholder': 'Select Location'}))

    area = ResourceSelect(resource_name='jobarea', queryset=JobArea.objects.all(), empty_label="",
                          widget=Select2Widget(select2_options={'placeholder': 'Select Area'}))

    hours = ResourceSelect(resource_name='hour', queryset=Hour.objects.all(), empty_label="",
                           widget=Select2Widget(select2_options={'placeholder': 'Select Hour'}))

    employment_type = ResourceSelect(resource_name='employmenttype', empty_label="",
                                     queryset=EmploymentType.objects.all(),
                                     widget=Select2Widget(select2_options={'placeholder': 'Select Employment Type'}))

    special_conditions = ResourceSelect(resource_name='specialcondition', empty_label="",
                                        queryset=SpecialCondition.objects.all(),
                                        widget=Select2Widget(select2_options=
                                        {'placeholder': 'Select Special Conditions'}))

    location = ResourceSelect(resource_name='joblocation', queryset=JobLocation.objects.all(), required=True,
                              empty_label="", widget=Select2Widget(select2_options={'placeholder': 'Select Location'}))

    class Meta:
        model = Job