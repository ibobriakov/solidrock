from django.forms.models import modelform_factory
from django_select2 import Select2Widget
from models import Feedback
from tastypie_rivets.forms import rivet_modelform_factory

__author__ = 'ir4y'

FeedbackForm = modelform_factory(Feedback,form=rivet_modelform_factory('contactus'),
                                 widgets={'priority':Select2Widget()})