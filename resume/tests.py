
from django.core.urlresolvers import reverse
from django.test import TestCase
from tastypie.test import ResourceTestCase
from dynamic_paper.tests.utils import PaperItemResourceTestMixin
from models import Resume, resume_template, resume_items_template


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class CoverLetterResourceTest(PaperItemResourceTestMixin, ResourceTestCase):
    def get_api_dispatch_list_url(self):
        return reverse('api_dispatch_list', kwargs={'api_name': 'v1', 'resource_name': 'resume'})

    def get_api_dispatch_detail_url(self, pk):
        return reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'resume', 'pk': pk})

    def setUp(self):
        super(CoverLetterResourceTest, self).setUp()

        # Create cover_letter
        self.resume_for_user1 = Resume.objects.create(name='cover letter for user1', owner=self.user1)
        self.resume_for_user2 = Resume.objects.create(name='cover letter for user2', owner=self.user2)

    def get_valid_json(self, test_item):
        return {
            'id': test_item.id,
            'paper': test_item.paper_id,
            'parent': test_item.parent_id if test_item.parent else False,
            'resource_uri': self.get_api_dispatch_detail_url(test_item.id),
            'type': "header",
            'value': test_item.paper.owner.username
        }

    def test_get_list_authorized(self):
        """
        Authorzied should see list with one item 'header' which value is username
        """
        #initial fileds count
        count = len(resume_template) + sum([len(l) for l in resume_items_template.itervalues()])

        #test for first user
        self.api_client.client.login(username=self.user1.username, password=self.password1)
        resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json')
        self.assertValidJSONResponse(resp)

        self.assertEqual(len(self.deserialize(resp)['objects']), count)

        #test for second user
        self.api_client.client.login(username=self.user2.username, password=self.password2)
        resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json')
        self.assertValidJSONResponse(resp)
        self.assertEqual(len(self.deserialize(resp)['objects']), count)

    def test_get_parent_filter_list_authorized(self):
        """
        Authorzied should see list with one item 'header' which value is username
        """
        #initial fileds count
        parent_length = {key: len(value) for key, value in resume_items_template.iteritems()}

        #test for first user
        self.api_client.client.login(username=self.user1.username, password=self.password1)
        for parent_type, child_count in parent_length.iteritems():
            parent_item = self.resume_for_user1.resumeitem_set.filter(type__name=parent_type)[0]
            resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json', data={'parent': parent_item.pk})
            self.assertValidJSONResponse(resp)
            self.assertEqual(len(self.deserialize(resp)['objects']), child_count)

        #test for second user
        self.api_client.client.login(username=self.user2.username, password=self.password2)
        for parent_type, child_count in parent_length.iteritems():
            parent_item = self.resume_for_user2.resumeitem_set.filter(type__name=parent_type)[0]
            resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json', data={'parent': parent_item.pk})
            self.assertValidJSONResponse(resp)
            self.assertEqual(len(self.deserialize(resp)['objects']), child_count)

    def test_subitem_add(self):
        self.api_client.client.login(username=self.user1.username, password=self.password1)
        resume_item = self.resume_for_user1.resumeitem_set.filter(type__name="list")[0]
        resp = self.api_client.post(self.get_api_dispatch_list_url(), format='json',
                                    data={"paper": self.resume_for_user1.id, "type": "text",
                                          "value": "", "parent": resume_item.id})
        self.assertHttpCreated(resp)
        self.assertIsNotNone(self.deserialize(resp)['id'])



