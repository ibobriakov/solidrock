from haystack import indexes
from employer.models import Job


__author__ = 'ir4y'


class JobIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)
    name = indexes.CharField(model_attr='name')
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')
    essential = indexes.MultiValueField()
    desireable = indexes.MultiValueField()

    def get_model(self):
        return Job

    def prepare_essential(self, obj):
        return [essential.essential for essential in obj.essential_set.all()]

    def prepare_desireable(self, obj):
        return [desireable.desireable for desireable in obj.desireable_set.all()]