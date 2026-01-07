"""
Mòdul de testing de l'exercici 2
"""

import unittest
from unittest.mock import patch

import pandas as pd

from src.modules.exercises.exercise_2.exercise_2 import exercise_2


class TestExercise2(unittest.TestCase):
    """
    Classe de testing per a l'exercici 2
    """

    @patch("src.modules.exercises.exercise_2.exercise_2.merge_dataframes")
    @patch("src.modules.exercises.exercise_2.exercise_2.group_dataframe")
    @patch("src.modules.exercises.exercise_2.exercise_2.delete_columns")
    @patch("src.modules.exercises.exercise_2.exercise_2.rename_columns")
    @patch("src.modules.exercises.exercise_2.exercise_2.pd.read_excel")
    def test_exercise_2_with_performance_file(
        self,
        mock_read_excel,
        mock_rename_columns,
        mock_delete_columns,
        mock_group_dataframe,
        mock_merge_dataframes,
    ) -> None:
        """
        Funció que simula el cas en què l'usuari carrega en primer lloc
        el fitxer rendiment_estudiants.xlsx.
        En aquesta funció se simulen totes les funcions cridades en el codi a través
        de mocks, juntament amb les dades que conté cada DataFrame.
        Finalment, la funció de test comprova que els dataframes siguin iguals,
        i que el flux sigui correcte.

        Args:
            mock_read_excel: Mock de la funció de llegir l'excel.
            mock_rename_columns: Mock de la funció que fa rename de les columnes.
            mock_delete_columns: Mock de la funció que elimina columnes.
            mock_group_dataframe: Mock de la funció que agrupa dataframes.
            mock_merge_dataframes: Mock de la funció que fa merge dels dataframes.

        Returns:
            None.
        """

        # Simulació del DataFrame d'entrada
        df_input = pd.DataFrame({"A": [1, 2]})
        df_input.source_file = "rendiment_estudiants.xlsx"

        # DataFrames simulats per a poder fer el test
        df_abandonment = pd.DataFrame({"B": [3, 4]})
        df_grouped_abandonment = pd.DataFrame({"C": [5]})
        df_grouped_performance = pd.DataFrame({"D": [6]})
        df_merged_expected = pd.DataFrame({"E": [7]})

        # Configuració dels mocks per a poder executar la funció de l'exercici 2
        mock_read_excel.return_value = df_abandonment
        mock_rename_columns.return_value = df_abandonment
        mock_delete_columns.side_effect = [
            df_abandonment,
            df_input
        ]
        mock_group_dataframe.side_effect = [
            df_grouped_abandonment,
            df_grouped_performance
        ]
        mock_merge_dataframes.return_value = df_merged_expected

        # Crida de l'exercici 2 amb les dades simulades
        result = exercise_2(df_input)

        # Validació que la funció torna el que esperem
        assert result.equals(df_merged_expected)

        # Validació de les crides siguin correctes, verificant el nombre de crides
        # i la integritat del flux
        mock_read_excel.assert_called_once_with("data/taxa_abandonament.xlsx")
        assert mock_group_dataframe.call_count == 2
        mock_merge_dataframes.assert_called_once()

    @patch("src.modules.exercises.exercise_2.exercise_2.pd.read_excel")
    def test_exercise_2_reads_other_file_when_abandonment_is_input(
        self,
        mock_read_excel
    ) -> None:
        """
        Funció que simula el cas en què l'usuari carrega el fitxer de la taxa_abandonament.xlsx.
        En aquest cas, només valida que es carregui correctament l'altre fitxer correctament.
        No valida la resta de lògica perquè en l'anterior ja ha estat validat.

        Args:
            mock_read_excel: Funció que mockeja la lectura de l'excel.

        Returns:
            None.
        """

        # Simulem els parametres d'entrada de la funció
        df_input = pd.DataFrame({"A": [1]})
        df_input.source_file = "taxa_abandonament.xlsx"

        mock_read_excel.return_value = pd.DataFrame()

        # Afegim tots els contexts dels mocks i fem que retornin sempre el mateix en l'execució
        # de la funció de l'exercici 2
        with patch(
            "src.modules.exercises.exercise_2.exercise_2.rename_columns",
            return_value=df_input
        ), patch(
            "src.modules.exercises.exercise_2.exercise_2.delete_columns",
            return_value=df_input
        ), patch(
            "src.modules.exercises.exercise_2.exercise_2.group_dataframe",
            return_value=df_input
        ), patch(
            "src.modules.exercises.exercise_2.exercise_2.merge_dataframes",
            return_value=df_input
        ):
            exercise_2(df_input)

        # Comprovem que es cridi un sol cop.
        mock_read_excel.assert_called_once_with(
            "data/rendiment_estudiants.xlsx"
        )
