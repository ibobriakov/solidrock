from tastypie.authentication import SessionAuthentication
from dynamic_paper.api import PaperResource, PaperItemResource
from dynamic_paper.api.validation import PaperItemValidation
from main.api import AuthorizationWithObjectPermissions
from models import CoverLetter, CoverLetterItem

__author__ = 'ir4y'


class CoverLetterResource(PaperResource):
    class Meta:
        queryset = CoverLetter.objects.all()
        resource_name = 'cover_letter_name'
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()


class CoverLetterItemResource(PaperItemResource):
    class Meta:
        queryset = CoverLetterItem.objects.all()
        resource_name = 'cover_letter'
        excludes = ['level', 'lft', 'rght', 'tree_id']
        always_return_data = True
        authentication = SessionAuthentication()
        authorization = AuthorizationWithObjectPermissions()
        validation = PaperItemValidation()