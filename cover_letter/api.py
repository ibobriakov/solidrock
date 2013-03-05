from tastypie.resources import ModelResource
from models import CoverLetterItem

__author__ = 'ir4y'


class CoverLetterItemResource(ModelResource):
    def get_object_list(self, request):
        if request.user.is_anonymous():
            return CoverLetterItem.objects.none()
        return CoverLetterItem.objects.filter(cover_letter__owner=request.user)

    class Meta:
        queryset = CoverLetterItem.objects.all()
        resource_name = 'cover_letter'