
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
        self.test_item_1 = CoverLetterItem.objects.create(paper=self.cover_letter_for_user1, type=header,
                                                          value=self.user1.username)
        self.test_item_2 = CoverLetterItem.objects.create(paper=self.cover_letter_for_user2, type=header,
                                                          value=self.user2.username)

        self.test_sub_item1 = CoverLetterItem.objects.create(paper=self.cover_letter_for_user1, type=header,
                                                             value=self.user1.username, parent=self.test_item_1)

    def get_valid_json(self, test_item):
        return {
            'id': test_item.id,
            'paper': test_item.paper_id,
            'parent': test_item.parent_id if test_item.parent else False,
            'resource_uri': self.get_api_dispatch_detail_url(test_item.id),
            'type': "header",
            'value': test_item.paper.owner.username
        }

    def test_get_list_authorzied(self):
        """
        Authorzied should see list with one item 'header' which value is username
        """
        #test for first user
        self.api_client.client.login(username=self.user1.username, password=self.password1)
        resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json')
        self.assertValidJSONResponse(resp)
        self.assertEqual(len(self.deserialize(resp)['objects']), 2)
        self.assertEqual(self.deserialize(resp)['objects'][0], self.get_valid_json(self.test_item_1))
        self.assertEqual(self.deserialize(resp)['objects'][1], self.get_valid_json(self.test_sub_item1))

        #test for second user
        self.api_client.client.login(username=self.user2.username, password=self.password2)
        resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json')
        self.assertValidJSONResponse(resp)
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)
        self.assertEqual(self.deserialize(resp)['objects'][0], self.get_valid_json(self.test_item_2))

    def test_filter_by_parent(self):
        """
        Authorized user1 should see test_sub_item1 for test_item_1
        """
        self.api_client.client.login(username=self.user1.username, password=self.password1)
        resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json', data={'parent': 'q'})
        self.assertHttpBadRequest(resp)
        self.assertEqual(self.deserialize(resp)['error'], "parent id isn't a number")

        resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json', data={'parent':
                                                                                          self.test_item_1.id})
        self.assertValidJSONResponse(resp)
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)
        self.assertEqual(self.deserialize(resp)['objects'][0], self.get_valid_json(self.test_sub_item1))

