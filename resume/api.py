from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from dynamic_paper.api import PaperItemResource
from models import ResumeItem

__author__ = 'ir4y'


class ResumeItemResource(PaperItemResource):
    class Meta:
        queryset = ResumeItem.objects.all()
        resource_name = 'resume'
        #always_return_data = True
        excludes = ['level', 'lft', 'rght', 'tree_id']
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()