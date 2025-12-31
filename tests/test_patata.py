import unittest
import src.modules.ex1_package.load_data as load_data

class TestPatata(unittest.TestCase):
    def test_test_patata(self):
        self.assertEqual(load_data.patata(), 'patata')