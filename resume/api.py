from dynamic_paper.api import PaperItemResource
from models import ResumeItem

__author__ = 'ir4y'


class ResumeItemResource(PaperItemResource):
    class Meta:
        queryset = ResumeItem.objects.all()
        resource_name = 'resume'
        excludes = ['level', 'lft', 'rght', 'tree_id']