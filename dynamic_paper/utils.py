from dynamic_paper.models import PaperItemType

__author__ = 'ir4y'


def get_paper_item(name):
    return  PaperItemType.objects.get_or_create(name=name)[0]