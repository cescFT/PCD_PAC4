"""
Mòdul de testing de l'exercici 1
"""

import unittest
import unittest.mock

from src.modules.exercises.exercise_1.read_file import read_file
from src.modules.exercises.exercise_1.explore_dataframe import explore_dataframe
from src.modules.exercises.exercise_1.exercise_1 import exercise_1
import pandas as pd

class TestReadFile(unittest.TestCase):
    """
    Classe de testing per a la lectura del fitxer
    """

    def test_read_file_ok_without_param(self) -> None:
        """
        Funció que revisa que es llegeixi el fitxer correctament sense paràmetres. Es moqueja l'input com si féssim clic
        a l'1.
        """

        with unittest.mock.patch('builtins.input', return_value="1"):
            self.assertEqual(type(read_file()), pd.DataFrame)

    def test_read_file_ok_with_param(self) -> None:
        """
        Funció que testeja que al passar-li un fitxer vàlid, retorni un dataframe.
        """

        self.assertEqual(type(read_file("data/rendiment_estudiants.xlsx")), pd.DataFrame)

class TestExploreDataframe(unittest.TestCase):
    """
    Classe que testeja el mòdul d'exploració del dataframe
    """

    def test_explore_dataframe(self) -> None:
        """
        Funció que testeja que al passar-li un fitxer vàlid, es carrega i es retorna correctament les dades demanades
        """
        df = read_file("data/rendiment_estudiants.xlsx")
        self.assertIsNone(explore_dataframe(df))

class TestExercise1(unittest.TestCase):
    """
    Classe de testing per a l'exercici 1
    """

    def test_exercise1_with_param(self) -> None:
        """
        Funció que testeja l'exercici 1 amb paràmetres paràmetres
        """
        with unittest.mock.patch('builtins.input', return_value="1"):
            self.assertEqual(type(exercise_1("data/rendiment_estudiants.xlsx")), pd.DataFrame)

    def test_exercise1_without_param(self):
        """
        Funció que testeja l'exercici 1 sense paràmetres paràmetres
        """
        self.assertEqual(type(exercise_1("data/rendiment_estudiants.xlsx")), pd.DataFrame)
