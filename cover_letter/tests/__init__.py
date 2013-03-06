
from django.core.urlresolvers import reverse
from tastypie.test import ResourceTestCase
from dynamic_paper.tests.utils import PaperItemResourceTestMixin
from dynamic_paper.models import PaperItemType
from ..models import CoverLetterItem, CoverLetter


class CoverLetterResourceTest(PaperItemResourceTestMixin, ResourceTestCase):
    def get_api_dispatch_list_url(self):
        return reverse('api_dispatch_list', kwargs={'api_name': 'v1', 'resource_name': 'cover_letter'})

    def get_api_dispatch_detail_url(self, pk):
        return reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'cover_letter', 'pk': pk})

    def setUp(self):
        super(CoverLetterResourceTest, self).setUp()

        # Create cover_letter
        self.cover_letter_for_user1 = CoverLetter.objects.create(name='cover letter for user1', owner=self.user1)
        self.cover_letter_for_user2 = CoverLetter.objects.create(name='cover letter for user2', owner=self.user2)

        # Create one item for cover_letter
        header = PaperItemType.objects.get_or_create(name='header')[0]
        self.test_item_1 = CoverLetterItem.objects.create(paper=self.cover_letter_for_user1, type=header, value=self.user1.username)
        self.test_item_2 = CoverLetterItem.objects.create(paper=self.cover_letter_for_user2, type=header, value=self.user2.username)

    def get_valid_json(self, test_item):
        return {
            'id': test_item.id,
            'paper': test_item.paper_id,
            'parent': False,
            'resource_uri': self.get_api_dispatch_detail_url(test_item.id),
            'type': "header",
            'value': test_item.paper.owner.username
        }