from collections import defaultdict
import copy
from main.api.validation import FormWithRequiredFiledValidation

__author__ = 'ir4y'


class ApplyToJobValidation(FormWithRequiredFiledValidation):
    def fix_pk_in_bundle(self, bundle):
        fixed_bundle = copy.copy(bundle)
        for field in ('resume', 'cover_letter'):
            if field in fixed_bundle.data and fixed_bundle.data[field]:
                fixed_bundle.data[field] = fixed_bundle.data[field].split("/")[-2]  # Get pk from uri
        return fixed_bundle

    def is_valid(self, bundle, request=None):
        errors = defaultdict(list)
        errors.update(super(ApplyToJobValidation, self).is_valid(self.fix_pk_in_bundle(bundle), request))
        user = bundle.request.user
        if 'resume' in errors or 'cover_letter' in errors:
            errors['error'] = ['Please select a Resume and Cover Letter']
        if not user.resume_set.count() or not user.coverletter_set.count():
            errors['error'] = ['You must create a Resume and Cover Letter before applying for a job']
        return errors