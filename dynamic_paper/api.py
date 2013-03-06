from tastypie.resources import ModelResource
from tastypie import fields

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
            orm_filters["parent__in"] = [int(pk) for pk in parent]

        return orm_filters

    class Meta:
        excludes = ['level', 'lft', 'rght', 'tree_id']