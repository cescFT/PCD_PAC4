"""
Suite per al testing del main
"""

import unittest
from tests.execution.test_main import TestMain

if __name__ == "__main__":
    suite = unittest.TestSuite()

    # Carrega els tests de cada classe
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestMain))

    # Executa la suite
    unittest.TextTestRunner(verbosity=2).run(suite)
