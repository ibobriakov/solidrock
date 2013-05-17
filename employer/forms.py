from tastypie_rivets import rivet_modelform_factory
from employer.models import Job


class JobForm(rivet_modelform_factory('job')):
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(args, kwargs)
        for field_name in self._meta.model.REQUIRED_FIELDS:
            label = self.fields[field_name].label
            self.fields[field_name].label = label+'*'
    class Meta:
        model = Job

