"""
Suite per al testing de l'exercici 3
"""

import unittest
from tests.exercise_3.test_exercise_3 import (
    TestExercise3,
    TestCreateSubplotWithSpecificData,
    TestPrepareDataOfPlot
)

if __name__ == "__main__":
    suite = unittest.TestSuite()

    # Carrega els tests de cada classe de test de l'exercici 3
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestExercise3))
    suite.addTests(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestCreateSubplotWithSpecificData)
    )
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestPrepareDataOfPlot))

    # Executa la suite
    unittest.TextTestRunner(verbosity=2).run(suite)
