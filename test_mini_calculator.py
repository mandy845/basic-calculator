import unittest
from main import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        add_method = add()
        self.assertEqual(2, add_method.add(1, 1), "adding 1")