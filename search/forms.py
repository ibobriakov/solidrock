from django import forms
from employer.models import JobCategory, JobSubCategory, JobLocation, JobArea

__author__ = 'ir4y'


class SearchForm(forms.Form):
    keywords = forms.CharField(required=False)
    executive_positions = forms.ChoiceField(required=False,
                                            choices=((0, "All Executive Positions"),
                                                     (1, "All Executive Positions")))
    categories = forms.ModelChoiceField(queryset=JobCategory.objects.none(),
                                        required=False, empty_label='Any Category')
    location = forms.ModelChoiceField(queryset=JobLocation.objects.none(),
                                      required=False, empty_label='All Australia')
    sub_categories = forms.ModelChoiceField(queryset=JobSubCategory.objects.none(),
                                            required=False, empty_label='Any Sub-Category')
    area = forms.ModelChoiceField(queryset=JobArea.objects.none(),
                                  required=False, empty_label='All')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['categories'].queryset = JobCategory.objects.all()
        self.fields['sub_categories'].queryset = JobSubCategory.objects.all()
        self.fields['location'].queryset = JobLocation.objects.all()
        self.fields['area'].queryset = JobArea.objects.all()
