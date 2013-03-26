
from django.core.urlresolvers import reverse
from tastypie.test import ResourceTestCase
from dynamic_paper.tests.utils import PaperItemResourceTestMixin
from models import Resume, resume_type_template


class ResumeResourceTest(PaperItemResourceTestMixin, ResourceTestCase):
    def get_api_change_name(self, pk):
        return reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'resume_name', 'pk': pk})

    def get_api_dispatch_list_url(self):
        return reverse('api_dispatch_list', kwargs={'api_name': 'v1', 'resource_name': 'resume'})

    def get_api_dispatch_detail_url(self, pk):
        return reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': 'resume', 'pk': pk})

    def setUp(self):
        super(ResumeResourceTest, self).setUp()

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
        Authorzied should see list
        """
        #test for first user
        self.api_client.client.login(username=self.user1.username, password=self.password1)
        resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json')
        self.assertValidJSONResponse(resp)

        #test for second user
        self.api_client.client.login(username=self.user2.username, password=self.password2)
        resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json')
        self.assertValidJSONResponse(resp)

    def test_get_parent_filter_list_authorized(self):
        """
        Authorzied should see list with one item 'header' which value is username
        """
        #initial fileds count
        parent_length = {key: len(inner_list) for key, inner_list in resume_type_template.iteritems()}

        #test for first user
        self.api_client.client.login(username=self.user1.username, password=self.password1)
        for parent_type, child_count in parent_length.iteritems():
            for parent_item in self.resume_for_user1.resumeitem_set.filter(type__name=parent_type + "_list"):
                resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json',
                                           data={'parent': parent_item.pk})
                self.assertValidJSONResponse(resp)
                json_result = self.deserialize(resp)
                self.assertEqual(len(json_result['objects']), 1)
                list_parent_id = json_result['objects'][0]['id']
                resp2 = self.api_client.get(self.get_api_dispatch_list_url(), format='json',
                                            data={'parent': list_parent_id})
                self.assertValidJSONResponse(resp2)
                self.assertEqual(len(self.deserialize(resp2)['objects']), child_count)

        #test for second user
        self.api_client.client.login(username=self.user2.username, password=self.password2)
        for parent_type, child_count in parent_length.iteritems():
            for parent_item in self.resume_for_user2.resumeitem_set.filter(type__name=parent_type + "_list"):
                resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json',
                                           data={'parent': parent_item.pk})
                self.assertValidJSONResponse(resp)
                json_result = self.deserialize(resp)
                self.assertEqual(len(json_result['objects']), 1)
                list_parent_id = json_result['objects'][0]['id']
                resp2 = self.api_client.get(self.get_api_dispatch_list_url(), format='json',
                                            data={'parent': list_parent_id})
                self.assertValidJSONResponse(resp2)
                self.assertEqual(len(self.deserialize(resp2)['objects']), child_count)

    def test_valid_subitem_add(self):
        self.api_client.client.login(username=self.user1.username, password=self.password1)

        first_list_container = self.resume_for_user1.resumeitem_set.filter(type__name__endswith="_list")[0]
        type_name = first_list_container.type.type_name()
        resp = self.api_client.post(self.get_api_dispatch_list_url(), format='json',
                                    data={"paper": self.resume_for_user1.id, "type": "container",
                                          "value": type_name, "parent": first_list_container.id})
        self.assertHttpCreated(resp)
        self.assertIsNotNone(self.deserialize(resp)['id'])

    def test_invalid_subitem_add(self):
        self.api_client.client.login(username=self.user1.username, password=self.password1)

        first_list_container = self.resume_for_user1.resumeitem_set.filter(type__name__endswith="_list")[0]
        second_list_container = self.resume_for_user1.resumeitem_set.filter(type__name__endswith="_list")\
            .exclude(type__name=first_list_container.type.name)[0]
        type_name = first_list_container.type.type_name()

        #add container with wrong parent
        resp = self.api_client.post(self.get_api_dispatch_list_url(), format='json',
                                    data={"paper": self.resume_for_user1.id, "type": "container",
                                          "value": type_name, "parent": second_list_container.id})
        self.assertHttpBadRequest(resp)

        #add not container
        resp = self.api_client.post(self.get_api_dispatch_list_url(), format='json',
                                    data={"paper": self.resume_for_user1.id, "type": "not_container",
                                          "value": type_name, "parent": first_list_container.id})
        self.assertHttpBadRequest(resp)

        #add container  with wrong value
        resp = self.api_client.post(self.get_api_dispatch_list_url(), format='json',
                                    data={"paper": self.resume_for_user1.id, "type": "container",
                                          "value": "wrong_value", "parent": first_list_container.id})
        self.assertHttpBadRequest(resp)

    def change_name(self):
        self.api_client.client.login(username=self.user1.username, password=self.password1)
        resp = self.api_client.put(self.get_api_change_name(self.resume_for_user1.pk),
                                   data={'name': 'Changed_Name'},
                                   format='json')
        self.assertHttpAccepted(resp)
        new_name = Resume.objects.get(pk=self.resume_for_user1.pk).name
        self.assertEqual(new_name, 'Changed_Name')
        resp = self.api_client.put(self.get_api_change_name(self.resume_for_user2.pk),
                                   data={'name': 'Changed_Name'},
                                   format='json')
        self.assertHttpUnauthorized(resp)
