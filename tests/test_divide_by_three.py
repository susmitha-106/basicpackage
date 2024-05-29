import unittest
from divide.by_three import divide_by_three

class TestDvideByThree(unittest.TestCase):
    def test_diived_by_three(self):
        self.assertEqual(divide_by_three(12), 4)
unittest.main()