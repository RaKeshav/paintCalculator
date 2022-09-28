import unittest
from paintCalc import *


class validatorTestor(unittest.TestCase):

    def test_int_validators(self):
        self.assertEqual(int_check(5, 10, 0, 'Integer'), False)  # The validator should except this
        self.assertEqual(int_check(12, 10, 0, 'Integer'), True)  # The validator shouldn't expect this

    def test_float_validators(self):
        self.assertEqual(int_check(6.2, 10, 0, 'Float'), False)  # The validator should except this
        self.assertEqual(int_check(12.2, 10, 0, 'Float'), True)  # The validator shouldn't expect this


if __name__ == '__main__':
    unittest.main()
