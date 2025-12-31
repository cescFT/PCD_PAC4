import unittest
from tests.test_patata import TestPatata


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPatata)
    unittest.TextTestRunner(verbosity=2).run(suite)
