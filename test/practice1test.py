import unittest
from main import practice1


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(practice1.add(1, 1), 2)
