import unittest
import unittest.mock

from src.modules.exercises.exercise_1.read_file import read_file
from src.modules.exercises.exercise_1.explore_dataframe import explore_dataframe
from src.modules.exercises.exercise_1.exercise_1 import exercise_1
import pandas as pd

class TestReadFile(unittest.TestCase):
    def test_read_file_ok_without_param(self):
        with unittest.mock.patch('builtins.input', return_value="1"):
            self.assertEqual(type(read_file()), pd.DataFrame)

    def test_read_file_ok_with_param(self):
        self.assertEqual(type(read_file("data/rendiment_estudiants.xlsx")), pd.DataFrame)

class TestExploreDataframe(unittest.TestCase):
    def test_explore_dataframe(self):
        df = read_file("data/rendiment_estudiants.xlsx")
        self.assertIsNone(explore_dataframe(df))

class TestExercise1(unittest.TestCase):
    def test_exercise1_without_param(self):
        with unittest.mock.patch('builtins.input', return_value="1"):
            self.assertEqual(type(exercise_1("data/rendiment_estudiants.xlsx")), pd.DataFrame)

    def test_exercise1_with_param(self):
        self.assertEqual(type(exercise_1("data/rendiment_estudiants.xlsx")), pd.DataFrame)