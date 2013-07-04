"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Job
from .utils import rotate_jobs

class SimpleTest(TestCase):
    def test_archiving(self):
        """
        Test job archiving
        """
        user = User.objects.create_user('user')
        job=Job()
        job.owner = user
        job.end_date = datetime.datetime.now() - datetime.timedelta(days=1)
        job.approved = True
        job.save()
        self.assertEqual(job.archived, False)
        rotate_jobs()
        job_after_update = Job.objects.get(id=job.id)
        self.assertEqual(job_after_update.archived, True)
        self.assertEqual(job_after_update.approved, False)
