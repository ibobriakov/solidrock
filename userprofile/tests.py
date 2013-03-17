"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from tastypie.test import ResourceTestCase
from userprofile.models import Employer, JobSeeker


class UserprofileResourceTestCase(ResourceTestCase):
    def setUp(self):
        self.job_seeker1, self.job_seeker1_password = self._add_user('job_seeker1', 'password1', 0)
        JobSeeker.objects.create(user=self.job_seeker1)
        self.job_seeker2, self.job_seeker2_password = self._add_user('job_seeker2', 'password2', 0)
        JobSeeker.objects.create(user=self.job_seeker2)
        
        self.employer1, self.employer1_password = self._add_user('employer1', 'password2', 1)
        Employer.objects.create(user=self.employer1, company="Company1", phone="987654321")
        self.employer2, self.employer2_password = self._add_user('employer2', 'password2', 1)
        Employer.objects.create(user=self.employer2, company="Company2", phone="987654321")

        super(UserprofileResourceTestCase, self).setUp()

    def _get_url(self, resource_name, pk=None):
        if not pk:
            return reverse('api_dispatch_list', kwargs={'api_name': 'v1', 'resource_name': resource_name})
        else:
            return reverse('api_dispatch_detail', kwargs={'api_name': 'v1', 'resource_name': resource_name, 'pk': pk})

    def _add_user(self, username, password, user_type):
        user = User.objects.create_user(username, username + '@example.com', password, user_type=user_type)
        return user, password

    def test_employer_profile_changes(self):
        self.api_client.client.login(username=self.employer1.username, password=self.employer1_password)
        resp = self.api_client.put(self._get_url('employer', self.employer1.profile.id),
                                   format='json',
                                   data={'company': "MyCompany1"})
        self.assertHttpAccepted(resp)
        self.assertEqual("MyCompany1", self.employer1.profile.company)

    def test_employer_profile_email_validation(self):
        self.api_client.client.login(username=self.employer1.username, password=self.employer1_password)
        resp = self.api_client.put(self._get_url('employer', self.employer1.profile.id),
                                   format='json',
                                   data={'email': "error"})
        self.assertHttpBadRequest(resp)
        self.assertTrue('email' in self.deserialize(resp)['employer'])

    def test_employer_profile_changes_by_other_user(self):
        self.api_client.client.login(username=self.employer2.username, password=self.employer2_password)
        resp = self.api_client.put(self._get_url('employer', self.employer1.profile.id),
                                   format='json',
                                   data={'company': "MyCompany1"})
        self.assertHttpUnauthorized(resp)
        
    def test_job_seeker_information_changes(self):
        self.api_client.client.login(username=self.job_seeker1.username, password=self.job_seeker1_password)
        resp = self.api_client.put(self._get_url('job_seeker_information',
                                                 self.job_seeker1.profile.personal_information.id),
                                   format='json',
                                   data={'first_name': "Jhon", "last_name": "Smith"})
        self.assertHttpAccepted(resp)
        # update job_seeker1 instance
        self.job_seeker1 = User.objects.get(pk=self.job_seeker1.pk)
        self.assertEqual("Jhon", self.job_seeker1.first_name)
        self.assertEqual("Smith", self.job_seeker1.last_name)

    def test_job_seeker_information_changes_by_other_user(self):
        self.api_client.client.login(username=self.job_seeker2.username, password=self.job_seeker2_password)
        resp = self.api_client.put(self._get_url('job_seeker_information',
                                                 self.job_seeker1.profile.personal_information.id),
                                   format='json',
                                   data={'first_name': "Jhon", "last_name": "Smith"})
        self.assertHttpUnauthorized(resp)

    def test_job_seeker_current_employment_changes(self):
        self.api_client.client.login(username=self.job_seeker1.username, password=self.job_seeker1_password)
        resp = self.api_client.put(self._get_url('job_seeker_current_employment',
                                                 self.job_seeker1.profile.current_employment.id),
                                   format='json',
                                   data={'name': "My Employment Name"})
        self.assertHttpAccepted(resp)
        self.assertEqual("My Employment Name", self.job_seeker1.profile.current_employment.name)

    def test_job_seeker_previous_employment_changes(self):
        self.api_client.client.login(username=self.job_seeker1.username, password=self.job_seeker1_password)
        resp = self.api_client.post(self._get_url('job_seeker_previous_employment'),
                                    format='json',
                                    data={'name': "My Employment Name",
                                          'position_title': "Programmer",
                                          'brief': "Write code",
                                          'leaving_reason': "I don't know"})
        self.assertHttpCreated(resp)
        resp = self.api_client.put(self._get_url('job_seeker_previous_employment', self.deserialize(resp)['id']),
                                   format='json',
                                   data={'name': "My Employment Name",
                                         'position_title': "Programmer",
                                         'brief': "Write code",
                                         'leaving_reason': "I need more cookies at lunch"})
        self.assertHttpAccepted(resp)
        self.assertEqual(self.deserialize(resp)['leaving_reason'], "I need more cookies at lunch")

    def test_job_seeker_referee_changes(self):
        self.api_client.client.login(username=self.job_seeker1.username, password=self.job_seeker1_password)
        resp = self.api_client.post(self._get_url('job_seeker_referee'),
                                    format='json',
                                    data={'name': "My Referee Name",
                                          'position_title': "Programmer",
                                          'phone_number': "00000",
                                          'email': "Invalid_email",
                                          'is_for_interview': False})
        self.assertHttpBadRequest(resp)
        self.assertTrue('email' in self.deserialize(resp)['job_seeker_referee'])

        resp = self.api_client.post(self._get_url('job_seeker_referee'),
                                    format='json',
                                    data={'name': "My Referee Name",
                                          'position_title': "Programmer",
                                          'phone_number': "00000",
                                          'email': "test@test.test",
                                          'is_for_interview': False})
        self.assertHttpCreated(resp)

        resp = self.api_client.put(self._get_url('job_seeker_referee', self.deserialize(resp)['id']),
                                   format='json',
                                   data={'name': "My Referee Name",
                                         'position_title': "Programmer",
                                         'phone_number': "00000",
                                         'email': "test@test.test",
                                         'is_for_interview': True})
        self.assertHttpAccepted(resp)
        self.assertTrue(self.deserialize(resp)['is_for_interview'])
        self.assertTrue(self.job_seeker1.profile.referees_set.count() == 1)
        self.assertTrue(self.job_seeker1.profile.referees_set.all()[0].is_for_interview)

