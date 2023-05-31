"""
class User
    __init__
        first_name str
        last_name str
        obtained_data bool (False)

    API:
        get_all_data -> method
            OK
            404

            (obtained_data becomes True if get_all_data_success_OK)
"""

import os
import sys
import unittest
from unittest.mock import patch

from user import User

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../src'
        )
    )
)


class TestUser(unittest.TestCase):
    def setUp(self):
        self.u1 = User('Lucas', 'de Matheu')
        self.u2 = User('Maria', 'Joaquina')

    def test_user_first_name_has_valid_attr(self):
        self.assertEqual(self.u1.first_name, 'Lucas')
        self.assertEqual(self.u2.first_name, 'Maria')

    def test_user_first_name_is_str(self):
        self.assertIsInstance(self.u1.first_name, str)
        self.assertIsInstance(self.u2.first_name, str)

    def test_user_last_name_has_valid_attr(self):
        self.assertEqual(self.u1.last_name, 'de Matheu')
        self.assertEqual(self.u2.last_name, 'Joaquina')

    def test_user_last_name_is_str(self):
        self.assertIsInstance(self.u1.last_name, str)
        self.assertIsInstance(self.u2.last_name, str)

    def test_user_obtained_data_starts_false(self):
        self.assertFalse(self.u1.obtained_data)
        self.assertFalse(self.u2.obtained_data)

    def test_get_all_data_success_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.u1.get_all_data(), 'Connected')
            self.assertTrue(self.u1.obtained_data)
            self.assertEqual(self.u2.get_all_data(), 'Connected')
            self.assertTrue(self.u2.obtained_data)

    def test_get_all_data_fail_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.u1.get_all_data(), 'Error 404')
            self.assertFalse(self.u1.obtained_data)
            self.assertEqual(self.u2.get_all_data(), 'Error 404')
            self.assertFalse(self.u2.obtained_data)

    def test_get_all_data_succed_and_fail_sequential(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.u1.get_all_data(), 'Connected')
            self.assertTrue(self.u1.obtained_data)
            self.assertEqual(self.u2.get_all_data(), 'Connected')
            self.assertTrue(self.u2.obtained_data)

            fake_request.return_value.ok = False

            self.assertEqual(self.u1.get_all_data(), 'Error 404')
            self.assertFalse(self.u1.obtained_data)
            self.assertEqual(self.u2.get_all_data(), 'Error 404')
            self.assertFalse(self.u2.obtained_data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
