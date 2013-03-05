from tastypie.resources import ModelResource
from tastypie import fields
from models import CoverLetterItem

__author__ = 'ir4y'


class CoverLetterItemResource(ModelResource):
    type = fields.CharField()
    parent = fields.IntegerField()
    paper = fields.IntegerField()

    def get_object_list(self, request):
        if request.user.is_anonymous():
            return CoverLetterItem.objects.none()
        return CoverLetterItem.objects.filter(cover_letter__owner=request.user)

    def dehydrate_type(self, bundle):
        return bundle.obj.type.name

    def dehydrate_parent(self, bundle):
        if bundle.obj.parent:
            return bundle.obj.parent.id
        else:
            return False

    def dehydrate_paper(self, bundle):
        return bundle.obj.cover_letter_id

    class Meta:
        queryset = CoverLetterItem.objects.all()
        resource_name = 'cover_letter'
        excludes = ['level', 'lft', 'rght', 'tree_id']