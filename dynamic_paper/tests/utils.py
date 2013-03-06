from django.contrib.auth.models import User


class PaperItemResourceTestMixin(object):

    def get_api_dispatch_list_url(self):
        raise NotImplemented

    def get_api_dispatch_detail_url(self, pk):
        raise NotImplemented

    def add_user(self, username, password):
        user = User.objects.create_user(username, username + '@example.com', password)
        return user, password

    def setUp(self):
        super(PaperItemResourceTestMixin, self).setUp()

        # Create a users.
        self.user1, self.password1 = self.add_user('user1', 'password1')
        self.user2, self.password2 = self.add_user('user2', 'password2')

    def test_get_list_unauthorzied(self):
        """
        Unauthorzied should see empty list
        """
        resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json')
        self.assertValidJSONResponse(resp)
        self.assertEqual(len(self.deserialize(resp)['objects']), 0)

    def test_get_list_authorzied(self):
        """
        Authorzied should see list with one item 'header' which value is username
        """

        #test for first user
        self.api_client.client.login(username=self.user1.username, password=self.password1)
        resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json')
        self.assertValidJSONResponse(resp)
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)
        self.assertEqual(self.deserialize(resp)['objects'][0], self.get_valid_json(self.test_item_1))

        #test for second user
        self.api_client.client.login(username=self.user2.username, password=self.password2)
        resp = self.api_client.get(self.get_api_dispatch_list_url(), format='json')
        self.assertValidJSONResponse(resp)
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)
        self.assertEqual(self.deserialize(resp)['objects'][0],self.get_valid_json(self.test_item_2))