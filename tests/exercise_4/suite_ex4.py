"""
Suite per al testing de l'exercici 4
"""

import unittest
from tests.exercise_4.test_exercise_4 import TestExercise4

if __name__ == "__main__":
    suite = unittest.TestSuite()

    # Carrega els tests de cada classe de test de l'exercici 4
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestExercise4))

    # Executa la suite
    unittest.TextTestRunner(verbosity=2).run(suite)
