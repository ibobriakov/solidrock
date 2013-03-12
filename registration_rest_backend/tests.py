"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from audioop import reverse
from django.contrib.auth.models import User
from registration.models import RegistrationProfile

from tastypie.test import ResourceTestCase


class RegisterResourceTestCase(ResourceTestCase):
    def setUp(self):
        self.user1, self.password1 = self.__add_user('user1', 'password1')
        super(RegisterResourceTestCase, self).setUp()

    def get_registert_url(self):
        return reverse('api_dispatch_list', kwargs={'api_name': 'v1', 'resource_name': 'register'})

    def get_activation_url(self):
        return reverse('api_dispatch_list', kwargs={'api_name': 'v1', 'resource_name': 'activation'})

    def __add_user(self, username, password):
        user = User.objects.create_user(username, username + '@example.com', password)
        return user, password

    def get_register_data(self, **kwargs):
        register_data = {
            'user_type': 'employer',
            'company_name': 'my_company',
            'email_address': 'employer@my_company.com',
            'phone_number': '+1234567',
            'password': 'password',
            're_password': 'password'
        }
        register_data.update(*kwargs)
        return register_data

    def test_authorized(self):
        self.api_client.client.login(username=self.user1.username, password=self.password1)
        resp = self.api_client.post(self.get_registert_url(), format='json',
                                    data=self.get_register_data())
        self.assertHttpBadRequest(resp)

    def test_unauthorized_register(self):
        #Register fail with password mismatch
        resp = self.api_client.post(self.get_registert_url(), format='json',
                                    data=self.get_register_data(re_password=''))
        self.assertHttpApplicationError(resp)

        #Register correct
        resp = self.api_client.post(self.get_registert_url(), format='json',
                                    data=self.get_register_data())
        self.assertHttpCreated(resp)

        #User should be unique
        resp = self.api_client.post(self.get_registert_url(), format='json',
                                    data=self.get_register_data())
        self.assertHttpApplicationError(resp)

        #Get new registered user
        new_user = User.objects.get(email=self.get_register_data()['email_address'])

        # Details of the returned user must match what went in.
        self.failUnless(new_user.check_password(self.get_register_data()['password']))
        self.assertEqual(new_user.email, self.get_register_data()['email_address'])

        # New user should can use resource.
        self.assertTrue(new_user.is_active)

    def test_valid_activation(self):
        #Register correct
        resp = self.api_client.post(self.get_registert_url(), format='json',
                                    data=self.get_register_data())
        self.assertHttpCreated(resp)

        valid_user = User.objects.get(email=self.get_register_data()['email_address'])
        valid_profile = RegistrationProfile.objects.get(user=valid_user)

        resp = self.api_client.post(self.get_registert_url(), format='json',
                                    data={'activation_key': valid_profile.activation_key})
        self.assertHttpAccepted(resp)

        # Fetch the profile again to verify its activation key has
        # been reset.
        valid_profile = RegistrationProfile.objects.get(user=valid_user)
        self.assertEqual(valid_profile.activation_key, RegistrationProfile.ACTIVATED)