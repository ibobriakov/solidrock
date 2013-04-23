from django_select2 import Select2Widget
from tastypie_rivets import rivet_modelform_factory
from employer.models import Job


class JobForm(rivet_modelform_factory('job')):
    class Meta:
        model = Job

