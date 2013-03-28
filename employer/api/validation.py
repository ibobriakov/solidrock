from collections import defaultdict
from tastypie.validation import FormValidation


class EmployerResourceValidation(FormValidation):
    requited_fields = ('name', 'title', 'description', 'location', 'hours', 'employment_type', 'contact_name')

    def is_valid(self, bundle, request=None):
        errors = defaultdict(list)
        errors.update(super(EmployerResourceValidation, self).is_valid(bundle, request))
        for key, value in bundle.data.items():
            if key in self.requited_fields and not value:
                errors[key].append('Field required')
        return errors