from collections import defaultdict
import copy
from main.api.validation import FormWithRequiredFiledValidation


class JobResourceValidation(FormWithRequiredFiledValidation):
    def fix_pk_in_bundle(self, bundle):
        fixed_bundle = copy.copy(bundle)
        for field in ('location', 'salary_range', 'hours', 'employment_type',
                      'special_conditions', 'executive_positions', 'area'):
            if field in fixed_bundle.data and fixed_bundle.data[field]:
                fixed_bundle.data[field] = fixed_bundle.data[field].split("/")[-2]  # Get pk from uri
        return fixed_bundle

    def is_valid(self, bundle, request=None):
        errors = defaultdict(list)
        errors.update(super(JobResourceValidation, self).is_valid(self.fix_pk_in_bundle(bundle), request))
        return errors