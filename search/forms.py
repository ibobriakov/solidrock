from django import forms
from django_select2 import Select2Widget
from employer.models import JobCategory, JobSubCategory, JobLocation, JobArea

__author__ = 'ir4y'


class SearchForm(forms.Form):
    keywords = forms.CharField(required=False)
    executive_positions = forms.ChoiceField(required=False,
                                            choices=(('', ''),  # empty option for select 2
                                                     (0, "All Executive Positions"),
                                                     (1, "All Executive Positions")),
                                            widget=Select2Widget(select2_options={'placeholder': 'All Positions'}))
    categories = forms.ModelChoiceField(queryset=JobCategory.objects.none(),
                                        required=False, empty_label='',
                                        widget=Select2Widget(select2_options={'placeholder': 'Any Category'}))
    location = forms.ModelChoiceField(queryset=JobLocation.objects.none(),
                                      required=False, empty_label='',
                                      widget=Select2Widget(select2_options={'placeholder': 'All Australia'}))
    sub_categories = forms.ModelChoiceField(queryset=JobSubCategory.objects.none(),
                                            required=False, empty_label='',
                                            widget=Select2Widget(select2_options={'placeholder': 'All'}))
    area = forms.ModelChoiceField(queryset=JobArea.objects.none(),
                                  required=False, empty_label='',
                                  widget=Select2Widget(select2_options={'placeholder': 'All'}))

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['categories'].queryset = JobCategory.objects.all()
        self.fields['sub_categories'].queryset = JobSubCategory.objects.all()
        self.fields['location'].queryset = JobLocation.objects.all()
        self.fields['area'].queryset = JobArea.objects.all()
