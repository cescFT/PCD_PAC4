"""
Mòdul de testing de l'exercici 4
"""

import unittest
from unittest.mock import patch, mock_open

import pandas as pd
import numpy as np

from src.modules.exercises.exercise_4.exercise_4 import exercise_4
from src.modules.exercises.exercise_4.statistics_functions import (
    analyze_dataset,
    calculate_metadata,
    calculate_global_stats,
    calculate_statistics_per_branch,
    calculate_ranking_by_branch,
    calculate_tendency_of_specific_branch,
    format_value,
    save_statistics,
)

class TestExercise4(unittest.TestCase):
    """
    Classe de tests de l'exercici 4 que testeja tots els submòduls que es criden en aquest exercici
    """

    sample_merged_df: pd.DataFrame
    """DataFrame senzill de test utilitzat en tots els tests."""

    def setUp(self) -> None:
        """
        Inicialització d'un DataFrame senzill que serà vàlid per a totes les
        funcions de tests.

        Args:
            None.

        Returns:
            None.
        """

        self.sample_merged_df = pd.DataFrame({
            "Curs Acadèmic": [2020, 2021, 2022, 2020, 2021, 2022],
            "Branca": ["A", "A", "A", "B", "B", "B"],
            "% Abandonament a primer curs": [30, 28, 25, 10, 10, 10],
            "Taxa rendiment": [60, 65, 70, 80, 80, 80],
        })

    def test_calculate_metadata(self) -> None:
        """
        Funció que testeja la funció del càlcul de les metadades del fitxer
        JSON.

        Args:
            None.

        Returns:
            None.
        """

        # Cridem la funció que calcula les metadades i validem que torna
        # les dades correctes.
        metadata = calculate_metadata(
            6,
            [2020, 2021, 2022]
        )

        # Validem a través dels asserts si retorna el que esperem.
        self.assertEqual(metadata["num_registros"], 6)
        self.assertEqual(metadata["periodo_temporal"], [2020, 2021, 2022])
        self.assertIn("fecha_analisis", metadata)

    def test_calculate_global_stats(self) -> None:
        """
        Funció que testeja la funció que analyze_dataset
        utilitza per a calcular les estadístiques globals
        que es demanen en l'enunciat.

        Args:
            None.

        Returns:
            None.
        """

        # Crida de la funció amb el DataFrame de test
        stats = calculate_global_stats(self.sample_merged_df)

        # Validacio que en la resposta estiguin els camps que s'esperen
        self.assertIn("abandono_medio", stats)
        self.assertIn("rendimiento_medio", stats)
        self.assertIn("correlacion_abandono_rendimiento", stats)

        # Comprovació simple que la correlació sigui un float
        self.assertIsInstance(
            stats["correlacion_abandono_rendimiento"],
            float
        )

    def test_calculate_statistics_per_branch(self) -> None:
        """
        Funció que testeja la subfunció del mòdul statistics_functions
        que és cridada pel analyze_dataset, i que el que fa és retornar
        informació referent a cada branca d'estudi.

        Args:
            None.

        Returns:
            None.
        """

        # Crida de la funció amb el dataframe de test
        stats = calculate_statistics_per_branch(self.sample_merged_df)

        # Validació que hi ha dades referents a cada branca d'estudi
        self.assertIn("A", stats)
        self.assertIn("B", stats)

        # Prenem d'exemple la branca A
        branch_a = stats["A"]

        # Validem que les dades que conté aquest, siguin el el que esperem
        self.assertEqual(branch_a["abandono_medio"], 27.67)
        self.assertEqual(branch_a["rendimiento_medio"], 65.0)
        self.assertEqual(branch_a["tendencia_abandono"], "decreixent")
        self.assertEqual(branch_a["tendencia_rendimiento"], "creixent")
        self.assertEqual(branch_a["años_anomalos"], [])


    def test_format_value(self) -> None:
        """
        Funció cridada dins de la subfució calculate_statistics_per_branch
        la qual el que fa és donar format al float, deixant-lo en dos decimals.

        Args:
            None.

        Returns:
            None.
        """

        # Validacions simples cridant la funció i comprovant que retorna el resultat que esperem
        self.assertEqual(format_value(np.float64(12.3456)), 12.35)
        self.assertEqual(format_value(np.float64(12.344)), 12.34)
        self.assertEqual(format_value(np.float64(10.0)), 10.0)

    def test_tendency_creixent(self) -> None:
        """
        Funció que testeja que la tendència sigui calculada correctament
        pel cas de la tendència creixent per a una branca d'estudi.

        Args:
             None.

        Returns:
            None.
        """

        # Seleccionem només una branca d'estudi de test.
        branch_a = self.sample_merged_df[
            self.sample_merged_df["Branca"] == "A"
        ]

        # Calculem la tendència
        result = calculate_tendency_of_specific_branch(
            branch_a,
            "Taxa rendiment"
        )

        # Validem que el resultat sigui creixent.
        self.assertEqual(result, "creixent")

    def test_tendency_decreixent(self) -> None:
        """
        Funció que testeja que la tendència sigui calculada correctament
        pel cas de la tendència decreixent per a una branca d'estudi.

        Args:
             None.

        Returns:
            None.
        """

        # Seleccionem només una branca d'estudi de test.
        branch_a = self.sample_merged_df[
            self.sample_merged_df["Branca"] == "A"
        ]

        # Calculem la tendència
        result = calculate_tendency_of_specific_branch(
            branch_a,
            "% Abandonament a primer curs"
        )

        # Validem que el resultat sigui decreixent.
        self.assertEqual(result, "decreixent")

    def test_tendency_estable(self) -> None:
        """
        Funció que testeja que la tendència sigui calculada correctament
        pel cas de la tendència estable per a una branca d'estudi.

        Args:
             None.

        Returns:
            None.
        """

        # Seleccionem només una branca d'estudi de test.
        branch_b = self.sample_merged_df[
            self.sample_merged_df["Branca"] == "B"
        ]

        # Calculem la tendència
        result = calculate_tendency_of_specific_branch(
            branch_b,
            "Taxa rendiment"
        )

        # Validem que el resultat sigui estable.
        self.assertEqual(result, "estable")

    def test_calculate_ranking_by_branch(self) -> None:
        """
        Funció de test que calcula el ranquing per branca d'estudi.

        Args:
            None.
        Returns:
            None.
        """

        # Cridem a la funció amb el DataFrame de test.
        ranking = calculate_ranking_by_branch(self.sample_merged_df)

        # Revisem amb els asserts que siguin les dades de sortida tal com esperem
        self.assertEqual(ranking["mejor_rendimiento"], ["B"])
        self.assertEqual(ranking["peor_rendimiento"], ["A"])
        self.assertEqual(ranking["mayor_abandono"], ["A"])
        self.assertEqual(ranking["menor_abandono"], ["B"])

    def test_analyze_dataset(self) -> None:
        """
        Funció que testeja la funció analyze_dataset, que és la que realment es crida en el mòdul
        corresponent a l'exercici 4.

        Args:
            None.

        Returns:
            None.
        """

        # Cridem la funció que analitza el dataset
        result = analyze_dataset(self.sample_merged_df)

        # Realitzem comprovacions per a comprovar que les claus estiguin
        # dins del result.
        self.assertIn("metadata", result)
        self.assertIn("estadisticas_globales", result)
        self.assertIn("analisis_por_rama", result)
        self.assertIn("ranking_ramas", result)

        # Comprovem que dins de les metadades estiguin els registres esperats.
        self.assertEqual(
            result["metadata"]["num_registros"],
            6
        )

    def test_save_statistics(self) -> None:
        """
        Funció que testeja que un JSON en format dict es desi correctament.

        Args:
            None.
        Returns:
            None.
        """

        # Mock d'un diccionari de test
        json_data = {"test": 123}

        # Comprovació que es desi en un fakepath en disc (mock)
        with patch("builtins.open", mock_open()):
            save_statistics(json_data, "fake/path/stats.json")

    def test_exercise_4_calls_analyze_and_save(self) -> None:
        """
        Funció que testeja la funció de l'exercici 4, la qual mockeja totes les funcions
        que necessita per a ser executada.

        Args:
            None.
        Returns:
            None.
        """

        # Fem un mock de les crides de analyze_dataset i de save_statistics
        # Cridem a la funció de l'exercici 4 amb el DataFrame de test
        # Revisem si es crida un cop ambdues funcions.
        with patch(
            "src.modules.exercises.exercise_4.exercise_4.analyze_dataset",
            return_value={"ok": True}
        ) as mock_analyze, patch(
            "src.modules.exercises.exercise_4.exercise_4.save_statistics"
        ) as mock_save:

            exercise_4(self.sample_merged_df)

            mock_analyze.assert_called_once_with(self.sample_merged_df)
            mock_save.assert_called_once()
