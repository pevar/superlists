import unittest
from django.test import TestCase


class SmokeTest(unittest.TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
