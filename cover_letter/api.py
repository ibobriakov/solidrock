from dynamic_paper.api import PaperItemResource
from models import CoverLetterItem

__author__ = 'ir4y'


class CoverLetterItemResource(PaperItemResource):
    class Meta:
        queryset = CoverLetterItem.objects.all()
        resource_name = 'cover_letter'
        excludes = ['level', 'lft', 'rght', 'tree_id']