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
        self.assertTrue("MyCompany1", self.employer1.profile.company)

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
        self.assertTrue("Jhon", self.job_seeker1.first_name)
        self.assertTrue("Smith", self.job_seeker1.last_name)

    def test_job_seeker_information_changes_by_other_user(self):
        self.api_client.client.login(username=self.job_seeker2.username, password=self.job_seeker2_password)
        resp = self.api_client.put(self._get_url('job_seeker_information',
                                                 self.job_seeker1.profile.personal_information.id),
                                   format='json',
                                   data={'first_name': "Jhon", "last_name": "Smith"})
        self.assertHttpUnauthorized(resp)


