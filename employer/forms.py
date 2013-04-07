from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django_select2 import Select2Widget
from main.forms import rivet_modelform_factory, url_choice_field_fabric
from models import Job, JobLocation, Hour, EmploymentType, SpecialCondition, JobArea

__author__ = 'jackdevil'


class JobForm(rivet_modelform_factory('job')):
    location = url_choice_field_fabric(lambda obj: reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'job', 'pk': obj.pk}))\
            (queryset=JobLocation.objects.all(), required=True, empty_label="",
             widget=Select2Widget(select2_options={'placeholder': 'Select Location'}))

    area = url_choice_field_fabric(lambda obj: reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'job', 'pk': obj.pk})) \
            (queryset=JobArea.objects.all(), empty_label="",
             widget=Select2Widget(select2_options={'placeholder': 'Select Area'}))

    hours = url_choice_field_fabric(lambda obj: reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'job', 'pk': obj.pk})) \
            (queryset=Hour.objects.all(), empty_label="",
             widget=Select2Widget(select2_options={'placeholder': 'Select Hour'}))

    employment_type = url_choice_field_fabric(lambda obj: reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'job', 'pk': obj.pk})) \
            (queryset=EmploymentType.objects.all(), empty_label="",
             widget=Select2Widget(select2_options={'placeholder': 'Select Employment Type'}))

    special_conditions = url_choice_field_fabric(lambda obj: reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'job', 'pk': obj.pk})) \
            (queryset=SpecialCondition.objects.all(), empty_label="",
             widget=Select2Widget(select2_options={'placeholder': 'Select Special Conditions'}))

    location = url_choice_field_fabric(lambda obj: reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'job', 'pk': obj.pk})) \
            (queryset=JobLocation.objects.all(), required=True, empty_label="",
             widget=Select2Widget(select2_options={'placeholder': 'Select Location'}))

    class Meta:
        model = Job
        widgets = {
            # 'location': Select2Widget(),
            'area': Select2Widget(),
            'hours': Select2Widget()
        }