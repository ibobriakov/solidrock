from collections import defaultdict
import copy
from tastypie.validation import FormValidation


class EmployerResourceValidation(FormValidation):
    requited_fields = ('name', 'title', 'description', 'location', 'hours', 'employment_type', 'contact_name')

    def fix_pk_in_bundle(self, bundle):
        fixed_bundle = copy.copy(bundle)
        for field in ('location', 'salary_range', 'hours', 'employment_type', 'special_conditions'):
            if field in fixed_bundle.data and fixed_bundle.data[field]:
                fixed_bundle.data[field] = fixed_bundle.data[field].split("/")[-2]  # Get pk from uri
        return fixed_bundle

    def is_valid(self, bundle, request=None):
        errors = defaultdict(list)
        errors.update(super(EmployerResourceValidation, self).is_valid(self.fix_pk_in_bundle(bundle), request))
        for key, value in bundle.data.items():
            if key in self.requited_fields and not value:
                errors[key].append('Field required')
        return errors