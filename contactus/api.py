from tastypie.resources import ModelResource
from tastypie.validation import FormValidation
from main.api import AuthorizationWithObjectPermissions
from models import Feedback
from forms import FeedbackForm

__all__ = ['FeedbackResource']
__author__ = 'ir4y'


class FeedbackResource(ModelResource):
    class Meta:
        queryset = Feedback.objects.all()
        resource_name = 'contactus'
        always_return_data = True
        allowed_methods = ('post',)
        authorization = AuthorizationWithObjectPermissions()
        validation = FormValidation(form_class=FeedbackForm)