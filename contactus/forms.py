from django.forms.models import modelform_factory
from django_select2 import Select2Widget
from main.forms import rivet_modelform_factory
from models import Feedback

__author__ = 'ir4y'

FeedbackForm = modelform_factory(Feedback,form=rivet_modelform_factory('contactus'),
                                 widgets={'priority':Select2Widget(select2_options={'placeholder':'Select Priority'})})