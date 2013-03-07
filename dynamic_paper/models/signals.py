__author__ = 'ir4y'


def get_signal_for_page(page_template):
    def create_page_paper(instance, created, **kwargs):
        if created:
            for item in page_template:
                item(instance).save()
    return create_page_paper


def get_signal_for_page_item(page_item_template):
    def create_page_item_childs(instance, created, **kwargs):
        if created:
            if instance.type.name in page_item_template:
                for item in page_item_template[instance.type.name]:
                    item(instance).save()
    return create_page_item_childs