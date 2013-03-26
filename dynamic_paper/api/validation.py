from collections import defaultdict
from tastypie.validation import Validation
from dynamic_paper.models import PaperItemType

__author__ = 'ir4y'


class PaperItemValidation(Validation):
    def is_valid(self, bundle, request=None):
        errors = defaultdict(list)
        if 'pk' not in bundle.data:
            if bundle.data["type"] != "container":
                errors["type"].append('Wrong type')
            klass = bundle.obj.__class__
            parent_item = klass.objects.get(pk=bundle.data['parent'])
            if parent_item.type.type_name() != bundle.data["value"]:
                errors["parent"].append('Wrong value for this parent')
        if PaperItemType.objects.filter(name=bundle.data['type']).count() != 1:
            errors["type"].append('Wrong type name')
        return errors