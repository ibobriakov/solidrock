"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from dynamic_paper.utils import get_paper_item


class SimpleTest(TestCase):
    def test_paper_model_functions(self):
        text = get_paper_item('text')
        self.assertFalse(text.is_list())
        self.assertEqual(text.type_name(), 'text')

        text = get_paper_item('phone_list')
        self.assertTrue(text.is_list())
        self.assertEqual(text.type_name(), 'phone')
