"""
Suite per al testing de l'exercici 1
"""

import unittest
from tests.exercise_1.test_exercise_1 import TestReadFile, TestExploreDataframe, TestExercise1

if __name__ == "__main__":
    """
    Càrrega dels elements de testeig de l'exercici 1
    """

    suite = unittest.TestSuite()

    # Carrega els tests de cada classe
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestReadFile))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestExploreDataframe))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestExercise1))

    # Executa la suite
    unittest.TextTestRunner(verbosity=2).run(suite)
