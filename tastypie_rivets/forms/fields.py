from itertools import chain
from django.forms import Widget
from django.forms.util import flatatt
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from tastypie_rivets.forms.model import url_choice_field_fabric
from tastypie_rivets.utils import get_api_url_fabric

__author__ = 'ir4y'


def ResourceSelect(resource_name=None, *args, **kwargs):
    return url_choice_field_fabric(get_api_url_fabric(resource_name))(*args, **kwargs)


class AngularSelect(Widget):
    allow_multiple_selected = False

    def __init__(self, attrs=None, choices=()):
        super(AngularSelect, self).__init__(attrs)
        # choices can be any iterable, but we may need to render this widget
        # multiple times. Thus, collapse it into a list so it can be consumed
        # more than once.
        self.choices = list(choices)

    def render(self, name, value, attrs=None, choices=()):
        ng_options = 'option[0] as option[1] for option in [{0}]'
        if value is None:
            value = ''
        additional = {
            'name': name,
            'ng-options': ng_options.format(self.render_options(choices))
        }
        final_attrs = self.build_attrs(attrs, **additional)
        output = [format_html('<select{0}>', flatatt(final_attrs))]
        output.append('</select>')
        return mark_safe('\n'.join(output))

    def render_options(self, choices):
        output = []
        for option_value, option_label in chain(self.choices, choices):
            if option_value == '':
                continue
            output.append("['{0}','{1}']".format(option_value, option_label))
        return ','.join(output)
