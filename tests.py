"""
Test cases
"""

#!coding: utf-8

from unittest import TestCase
from app.common.lib import get_message, get_json, auth


class HelloworldTestCase(TestCase):
    """ Tests"""
    def test_helloworld(self):
        """ Test get_message """
        self.assertEqual(get_message(), 'Hello World!')

    def test_json(self):
        """ Test json """
        self.assertEqual(get_json(), {'key':'value'})

    def test_auth(self):
        """ Test authorization """
        self.assertEqual(auth('alexander'), 'alexander')
        self.assertEqual(auth('123'), None)
        self.assertNotEqual(auth('123'), '123')
