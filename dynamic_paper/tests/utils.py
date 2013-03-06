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
        Unauthorzied shouldn't see anything
        """
        self.assertHttpUnauthorized(self.api_client.get(self.get_api_dispatch_list_url(), format='json'))