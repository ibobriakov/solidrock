from django import forms
from employer.models import JobCategory, JobSubCategory, JobLocation

__author__ = 'ir4y'


class SearchForm(forms.Form):
    keywords = forms.CharField(required=False)
    executive_positions = forms.ChoiceField(required=False,
                                            choices=((0, "All Executive Positions"),
                                                     (1, "All Executive Positions")))
    category = forms.ModelChoiceField(queryset=JobCategory.objects.none(),
                                      required=False, empty_label='Any Category')
    location = forms.ModelChoiceField(queryset=JobLocation.objects.none(),
                                      required=False, empty_label='All Australia')
    sub_category = forms.ModelChoiceField(queryset=JobSubCategory.objects.none(),
                                          required=False, empty_label='Any Sub-Category')
    area = forms.ChoiceField(required=False,
                             choices=((0, "Any Area"),
                                      (1, "Any Area")))

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = JobCategory.objects.all()
        self.fields['sub_category'].queryset = JobSubCategory.objects.all()
        self.fields['location'].queryset = JobLocation.objects.all()
