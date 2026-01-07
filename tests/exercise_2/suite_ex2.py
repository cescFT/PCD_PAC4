"""
Suite per al testing de l'exercici 2
"""

import unittest
from tests.exercise_2.test_exercise_2 import TestExercise2

if __name__ == "__main__":
    suite = unittest.TestSuite()

    # Carrega els tests de la classe de test de l'exercici 2
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestExercise2))

    # Executa la suite
    unittest.TextTestRunner(verbosity=2).run(suite)
