from tastypie.authentication import SessionAuthentication
from dynamic_paper.api import PaperItemResource
from main.api import AuthorizationWithObjectPermissions
from models import CoverLetterItem

__author__ = 'ir4y'


class CoverLetterItemResource(PaperItemResource):
    class Meta:
        queryset = CoverLetterItem.objects.all()
        resource_name = 'cover_letter'
        excludes = ['level', 'lft', 'rght', 'tree_id']
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()