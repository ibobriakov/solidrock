from django import forms
from django_select2 import Select2Widget
from employer.models import JobCategory, JobSubCategory, JobLocation, JobArea, JobExecutivePositions,\
    Hour, EmploymentType

__author__ = 'ir4y'


class SearchForm(forms.Form):
    keywords = forms.CharField(required=False)
    executive_positions = forms.BooleanField(label="Executive Positions", required=False)
    categories = forms.ModelChoiceField(queryset=JobCategory.objects.none(),
                                        required=False, empty_label='',
                                        widget=Select2Widget(select2_options={'placeholder': 'Any Category',
                                                                              'allowClear': True}))

    sub_categories = forms.ModelChoiceField(queryset=JobSubCategory.objects.none(),
                                            required=False, empty_label='',
                                            widget=Select2Widget(select2_options={'placeholder': 'All',
                                                                                  'allowClear': True}))
    location = forms.ModelChoiceField(queryset=JobLocation.objects.none(),
                                      required=False, empty_label='',
                                      widget=Select2Widget(select2_options={'placeholder': 'All Australia',
                                                                            'allowClear': True}))
    area = forms.ModelChoiceField(queryset=JobArea.objects.none(),
                                  required=False, empty_label='',
                                  widget=Select2Widget(select2_options={'placeholder': 'All',
                                                                        'allowClear': True}))
    # more options
    featured = forms.BooleanField(label="Featured Jobs", required=False)
    hours = forms.ModelChoiceField(queryset=Hour.objects.none(),
                                   required=False, empty_label='',
                                   widget=Select2Widget(select2_options={'placeholder': 'All',
                                                                         'allowClear': True}))
    employment_type = forms.ModelChoiceField(queryset=EmploymentType.objects.none(),
                                             required=False, empty_label='',
                                             widget=Select2Widget(select2_options={'placeholder': 'All',
                                                                                   'allowClear': True}))
    salary_min = forms.IntegerField(label='Salary Range Min', required=False)
    salary_max = forms.IntegerField(label='Salary Range Max', required=False)

    more_options_fields_names = ('featured',
                                 'hours',
                                 'employment_type',
                                 'salary_min',
                                 'salary_max')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['executive_positions'].queryset = JobExecutivePositions.objects.all()
        self.fields['categories'].queryset = JobCategory.objects.all()
        self.fields['sub_categories'].queryset = JobSubCategory.objects.all()
        self.fields['location'].queryset = JobLocation.objects.all()
        self.fields['area'].queryset = JobArea.objects.all()

        self.fields['hours'].queryset = Hour.objects.all()
        self.fields['employment_type'].queryset = EmploymentType.objects.all()

    def default_fields(self):
        """
        Returns a list of BoundField objects that aren't hidden fields.
        The opposite of the hidden_fields() method.
        """
        return [field for field in self if not field.is_hidden and field.name not in self.more_options_fields_names]

    def more_options_fileds(self):
        return [field for field in self if not field.is_hidden and field.name in self.more_options_fields_names]
