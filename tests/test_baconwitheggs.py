"""
TDD - Test Driven Development

First step (RED): Test first to see it fail;

Second step (GREEN): Develop and see it work.

Third step (Refactor): Improve it.
"""

import os
import sys
import unittest

from baconwitheggs import bacon_with_eggs

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../src'
        )
    )
)


class TestBaconWithEggs(unittest.TestCase):
    def test_bacon_with_eggs_must_raise_assertion_error_if_n_not_int(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs('0')

    def test_bacon_with_eggs_must_return_bacon_with_eggs_if_input_is_multiple_of_3_and_5(self):  # noqa
        inputs = (15, 30, 45, 60)
        output = 'Bacon with Eggs'

        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(
                    bacon_with_eggs(input),
                    output,
                    msg=f'"{input}" did not return "{output}"'
                )

    def test_bacon_with_eggs_must_return_starving_if_input_is_not_multiple_of_either_3_or_5(self):  # noqa
        inputs = (1, 2, 4, 7, 8)
        output = 'Starving'

        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(
                    bacon_with_eggs(input),
                    output,
                    msg=f'"{input}" did not return "{output}"'
                )

    def test_bacon_with_eggs_must_return_bacon_if_input_is_multiple_of_3_only(self):  # noqa
        inputs = (3, 6, 9, 12, 18, 21)
        output = 'Bacon'

        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(
                    bacon_with_eggs(input),
                    output,
                    msg=f'"{input}" did not return "{output}"'
                )

    def test_bacon_with_eggs_must_return_eggs_if_input_is_multiple_of_5_only(self):  # noqa
        inputs = (5, 10, 20, 25, 35)
        output = 'Eggs'

        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(
                    bacon_with_eggs(input),
                    output,
                    msg=f'"{input}" did not return "{output}"'
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)
