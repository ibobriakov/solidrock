from dynamic_paper.utils import get_paper_item

__author__ = 'ir4y'


def get_signal_for_page(page_template):
    def create_page_paper(instance, created, **kwargs):
        if created:
            for item in page_template:
                item(instance).save()
    return create_page_paper


def get_signal_for_page_item(page_type_template):
    def create_page_item_childs(instance, created, **kwargs):
        if created:
            if instance.type.name.endswith('_list'):
                klass = instance.__class__
                klass.objects.create(type=get_paper_item('container'), value=instance.type.name[:-5],
                                     paper=instance.paper, parent=instance)
            elif instance.type.name == "container":
                for item in page_type_template[instance.value]:
                    item(instance).save()
    return create_page_item_childs