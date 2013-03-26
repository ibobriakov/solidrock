from tastypie.authentication import SessionAuthentication
from dynamic_paper.api import PaperResource, PaperItemResource
from dynamic_paper.api.validation import PaperItemValidation
from main.api import AuthorizationWithObjectPermissions
from models import Resume, ResumeItem

__author__ = 'ir4y'


class ResumeResource(PaperResource):
    class Meta:
        queryset = Resume.objects.all()
        resource_name = 'resume_name'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()


class ResumeItemResource(PaperItemResource):
    class Meta:
        queryset = ResumeItem.objects.all()
        resource_name = 'resume'
        excludes = ['level', 'lft', 'rght', 'tree_id']
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = PaperItemValidation()