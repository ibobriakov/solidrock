from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie.exceptions import BadRequest, Unauthorized
from tastypie import fields
from models import PaperItemType


__author__ = 'ir4y'


class PaperItemResource(ModelResource):
    type = fields.CharField()
    parent = fields.IntegerField()
    paper = fields.IntegerField()

    def get_object_list(self, request):
        query_set = super(PaperItemResource, self).get_object_list(request)
        if request.user.is_anonymous():
            return query_set.none()
        return query_set.filter(paper__owner=request.user)

    def dehydrate_type(self, bundle):
        return bundle.obj.type.name

    def hydrate(self, bundle):
        if not bundle.obj.pk:
            bundle.obj.paper_id = bundle.data['paper']
            bundle.obj.parent_id = bundle.data['parent']
            bundle.obj.type_id = PaperItemType.objects.get(name=bundle.data['type']).id
        return bundle

    def dehydrate_parent(self, bundle):
        if bundle.obj.parent:
            return bundle.obj.parent.id
        else:
            return False

    def dehydrate_paper(self, bundle):
        return bundle.obj.paper_id

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        parent = filters.pop('parent', None)
        orm_filters = super(PaperItemResource, self).build_filters(filters)
        if parent:
            if len(parent) != 1:
                raise BadRequest("To many parents")
            try:
                pk = int(parent[0])
            except ValueError:
                raise BadRequest("parent id isn't a number")
            orm_filters["parent__pk"] = pk
        return orm_filters

    class Meta:
        excludes = ['level', 'lft', 'rght', 'tree_id']