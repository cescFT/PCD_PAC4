"""
Mòdul de testing de l'exercici 3
"""

import unittest
from unittest.mock import patch, MagicMock

import pandas as pd
import matplotlib.pyplot as plt

from src.modules.exercises.exercise_3.exercise_3 import exercise_3
from src.modules.exercises.exercise_3.subplot_create import (
    create_subplot_with_specific_data,
    prepare_data_of_plot
)

class TestExercise3(unittest.TestCase):
    """
    Classe de testing per a l'exercici 3, per la funció principal.
    """

    @patch("src.modules.exercises.exercise_3.exercise_3.os.makedirs")
    @patch("src.modules.exercises.exercise_3.exercise_3.plt.savefig")
    @patch("src.modules.exercises.exercise_3.exercise_3.plt.subplots")
    @patch("src.modules.exercises.exercise_3.exercise_3.create_subplot_with_specific_data")
    def test_exercise_3_generates_and_saves_plot(
        self,
        mock_create_subplot,
        mock_subplots,
        mock_savefig,
        mock_makedirs
    ) -> None:
        """
        Funció que testeja l'execució principal de l'exercici 3, tot comprovant la generació
        dels subplots, creant una llegenda única i la resta de configuracions, i finalment desant
        la figura.

        Args:
            mock_create_subplot: Mock que simula la creació de subplots.
            mock_subplots: Mock que simula la funció de generar subplots.
            mock_savefig: Mock que simula desar la imatge al path corresponent.
            mock_makedirs: Mock que simula la funció que crea directoris.

        Returns:
            None.
        """

        # Simulem els paràmetres d'entrada en un DataFrame improvitzat
        # amb les dades inventades per al test.
        df_grouped = pd.DataFrame({
            "Curs Acadèmic": ["2020-2021", "2021-2022"],
            "Branca": ["Enginyeria", "Ciències"],
            "% Abandonament a primer curs": [20.5, 18.3],
            "Taxa rendiment": [75.2, 78.1]
        })

        # Mocks de les funcions de matplotlib per a poder dur a terme el test
        mock_fig = MagicMock()
        mock_ax1 = MagicMock()
        mock_ax2 = MagicMock()
        mock_subplots.return_value = (mock_fig, [mock_ax1, mock_ax2])

        # Retorn del primer subplot, amb les dades necessaries per a poder fer el plot
        mock_create_subplot.return_value = {
            "all_lines": ["line1", "line2"],
            "all_labels": ["Enginyeria", "Ciències"]
        }

        # Crida de la funció de l'exercici 3 amb el dataframe agrupat
        exercise_3(df_grouped)

        # Comprovem que la funció que genera els subplots hagi estat cridada un
        # sol cop amb els paràmetres corresponents.
        mock_subplots.assert_called_once_with(
            nrows=2,
            ncols=1,
            figsize=(14, 10),
            sharex=True
        )

        # Comprovació que la funció auxiliar de creació dels subplots es crida dues vegades.
        self.assertEqual(mock_create_subplot.call_count, 2)

        # Comprobació que la funció de crear directoris es crida un cop.
        mock_makedirs.assert_called_once_with(
            "src/img/",
            exist_ok=True
        )

        # Comprovació que s'ha cridat un sol cop la crida a desar la imatge.
        mock_savefig.assert_called_once_with(
            "src/img/evolucio_francesc_ferre_tarres.png",
            dpi=300,
            bbox_inches="tight"
        )

        # Es crea la llegenda global, que es crida un sol cop.
        mock_fig.legend.assert_called_once()

        # S'aplica el layout, que es crida un sol cop.
        mock_fig.tight_layout.assert_called_once()


class TestPrepareDataOfPlot(unittest.TestCase):
    """
    Tests unitaris de la funció prepare_data_of_plot del mòdul subplot_create
    """

    def test_prepare_data_of_plot_groups_and_means_correctly(self) -> None:
        """
        Comprova que la funció agrupa per Curs Acadèmic i Branca
        i calcula correctament la mitjana. En aquest cas comprovat amb el
        % d'abandonament a primer curs

        Args:
            None.

        Returns:
            None.
        """

        # Mock d'un dataframe amb dades inventades per a validar que les dades siguin correctes
        df = pd.DataFrame({
            "Curs Acadèmic": ["2020", "2020", "2021"],
            "Branca": ["Enginyeria", "Enginyeria", "Ciències"],
            "% Abandonament a primer curs": [20, 30, 10]
        })


        # Mock de la sortida esperada
        expected_output = pd.DataFrame({
            "Curs Acadèmic": ["2020", "2021"],
            "Branca": ["Enginyeria", "Ciències"],
            "% Abandonament a primer curs": [25.0, 10.0]
        })

        # Cridem a la funció, tot indicant-li els paràmetres d'entrada esperats
        result = prepare_data_of_plot(
            df,
            "% Abandonament a primer curs"
        )

        # Validem si els DataFrame son iguals a través de la funció de testing de pandas.
        pd.testing.assert_frame_equal(result, expected_output)


class TestCreateSubplotWithSpecificData(unittest.TestCase):
    """
    Tests unitaris de la funció create_subplot_with_specific_data
    """

    def test_create_subplot_returns_lines_and_labels(self) -> None:
        """
        Comprova que es creen tantes línies com branques
        i que el que retorna conté les línies i etiquetes correctes.

        Args:
            None.

        Returns:
            None.
        """

        # Mock d'un DataFrame de test per a fer les proves
        df_grouped = pd.DataFrame({
            "Curs Acadèmic": ["2020", "2021", "2020", "2021"],
            "Branca": ["Enginyeria", "Enginyeria", "Ciències", "Ciències"],
            "Taxa rendiment": [70, 75, 80, 85]
        })

        # Creació d'un subplot de test per a fer el testeig de la funció.
        fig, ax = plt.subplots()

        # Crida de la funció amb els paràmetres necessaris i que tenen sentit en aquest test.
        result = create_subplot_with_specific_data(
            axes=ax,
            df_grouped=df_grouped,
            study_factor="Taxa rendiment",
            study_type=["Enginyeria", "Ciències"],
            title="Test title",
            y_label="Test Y",
            x_label="Test X"
        )

        # Conjunt d'asserts sobre el result que permeten conèixer si el resultat és l'esperat
        self.assertIn("all_lines", result)
        self.assertIn("all_labels", result)
        self.assertEqual(len(result["all_lines"]), 2)
        self.assertEqual(result["all_labels"], ["Enginyeria", "Ciències"])

        # Conjunt d'asserts que es fan sobre l'axes per a poder saber si s'ha generat correctament
        # tal com s'espera.
        self.assertEqual(ax.get_title(), "Test title")
        self.assertEqual(ax.get_ylabel(), "Test Y")
        self.assertEqual(ax.get_xlabel(), "Test X")

        # Al ser un test, simplement eliminem la figura.
        plt.close(fig)

    def test_create_subplot_without_x_label(self) -> None:
        """
        Comprova que la funció funciona correctament
        quan no s'especifica l'etiqueta de l'eix X.

        Args:
            None.

        Returns:
            None.
        """

        # Creació d'un DataFrame de test mock per a poder fer el testeig
        df_grouped = pd.DataFrame({
            "Curs Acadèmic": ["2020"],
            "Branca": ["Enginyeria"],
            "% Abandonament a primer curs": [15]
        })

        # Creació d'un subplot de test per a fer el testeig de la funció.
        fig, ax = plt.subplots()

        # Crida de la funció amb els paràmetres necessaris per a que funcioni i sense
        # el valor de la label de la coordenada X.
        result = create_subplot_with_specific_data(
            axes=ax,
            df_grouped=df_grouped,
            study_factor="% Abandonament a primer curs",
            study_type=["Enginyeria"],
            title="Sense xlabel",
            y_label="%"
        )

        # Conjunt d'asserts per a conèixer si el result és tal com s'espera.
        self.assertEqual(len(result["all_lines"]), 1)
        self.assertEqual(result["all_labels"], ["Enginyeria"])

        # Al ser un test, simplement eliminem la figura.
        plt.close(fig)
