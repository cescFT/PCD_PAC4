"""
Classe de testing que testeja la funció principal main
"""

# Referències:
# * Teoria U6
# * https://docs.python.org/es/dev/library/unittest.mock.html
# * https://docs.python.org/3/library/unittest.mock.html
# * https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock

import unittest
from unittest.mock import patch, MagicMock
from src.execution.main import main


class TestMain(unittest.TestCase):
    """
    Classe que testeja tota la funció main.
    """

    @patch("src.execution.main.argparse.ArgumentParser.parse_args")
    @patch("src.execution.main.exercise_1.exercise_1")
    @patch("src.execution.main.exercise_2.exercise_2")
    @patch("src.execution.main.exercise_3.exercise_3")
    @patch("src.execution.main.exercise_4.exercise_4")
    @patch("src.execution.main.sys.exit")
    def test_no_arguments_executes_all(
        self,
        mock_exit,
        mock_ex4,
        mock_ex3,
        mock_ex2,
        mock_ex1,
        mock_parse_args
    ) -> None:
        """
        Test de la funció main() sense passar arguments per línia de comanda.
    
        Aquest test comprova que, quan no es passen arguments es criden tots els exercicis en ordre ascendent. Es
        simulen les funcions dels exercisis i al final es comprova el sys.exit(0), indicant final correcte d'execució.
    
        Args:
             mock_exit: Mock de sys.exit per evitar sortir del test realment.
             mock_ex4: Mock de la funció exercise_4.
             mock_ex3: Mock de la funció exercise_3.
             mock_ex2: Mock de la funció exercise_2.
             mock_ex1: Mock de la funció exercise_1.
             mock_parse_args: Mock de parse_args per simular els arguments de línia de comanda.
    """
        mock_parse_args.return_value = MagicMock(ex=None, file=None)
        mock_ex1.return_value = "df_read"
        mock_ex2.return_value = "merged_df"

        main()

        mock_ex1.assert_called_once_with("")
        mock_ex2.assert_called_once_with("df_read")
        mock_ex3.assert_called_once_with("merged_df")
        mock_ex4.assert_called_once_with("merged_df")
        mock_exit.assert_called_once_with(0)

    @patch("src.execution.main.argparse.ArgumentParser.parse_args")
    def test_invalid_exercise_number(self, mock_parse_args) -> None:
        """
        Funció que comprova el codi de passar-li un valor erroni al main.
        Args:
            mock_parse_args: Mock dels arguments passats per línia de comanda
        """
        mock_parse_args.return_value = MagicMock(ex=10, file=None)

        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(cm.exception.code, 1)

    @patch("src.execution.main.argparse.ArgumentParser.parse_args")
    @patch("src.execution.main.os.path.isfile", return_value=False)
    @patch("src.execution.main.os.path.exists", return_value=False)
    def test_invalid_file_path(self, mock_exists, mock_isfile, mock_parse_args) -> None:
        """
        Test de la funció main() quan se li passa un fitxer invàlid amb l'argument -file.
        
        Args: 
             mock_exists: Mock de os.path.exists per controlar l'existència del fitxer.
             mock_isfile: Mock de os.path.isfile per controlar si és un fitxer.
             mock_parse_args: Mock de parse_args per simular els arguments de línia de comanda.
        """
        mock_parse_args.return_value = MagicMock(ex=None, file="fake.xlsx")

        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(cm.exception.code, 1)

    @patch("src.execution.main.argparse.ArgumentParser.parse_args")
    @patch("src.execution.main.exercise_1.exercise_1")
    @patch("src.execution.main.exercise_2.exercise_2")
    @patch("src.execution.main.exercise_3.exercise_3")
    @patch("src.execution.main.exercise_4.exercise_4")
    @patch("src.execution.main.sys.exit")
    def test_only_exercise_1(
        self,
        mock_exit,
        mock_ex4,
        mock_ex3,
        mock_ex2,
        mock_ex1,
        mock_parse_args
    ) -> None:
        """
        Funció que valida només un exercici específic, en concret l'exercici 1.
        
        Args:
             mock_exit: Mock de sys.exit per evitar sortir del test realment.
             mock_ex4: Mock de la funció exercise_4.
             mock_ex3: Mock de la funció exercise_3.
             mock_ex2: Mock de la funció exercise_2.
             mock_ex1: Mock de la funció exercise_1.
             mock_parse_args: Mock de parse_args per simular els arguments de línia de comanda.
        :return: 
        """

        mock_parse_args.return_value = MagicMock(ex=1, file=None)
        mock_ex1.return_value = "df_read"

        main()

        mock_ex1.assert_called_once_with("")
        mock_ex2.assert_not_called()
        mock_ex3.assert_not_called()
        mock_ex4.assert_not_called()
        mock_exit.assert_called_once_with(0)

    @patch("src.execution.main.argparse.ArgumentParser.parse_args")
    @patch("src.execution.main.os.path.isfile", return_value=True)
    @patch("src.execution.main.os.path.exists", return_value=True)
    @patch("src.execution.main.exercise_1.exercise_1")
    @patch("src.execution.main.exercise_2.exercise_2")
    @patch("src.execution.main.exercise_3.exercise_3")
    @patch("src.execution.main.exercise_4.exercise_4")
    @patch("src.execution.main.sys.exit")
    def test_full_execution_with_file(
        self,
        mock_exit,
        mock_ex4,
        mock_ex3,
        mock_ex2,
        mock_ex1,
        mock_exists,
        mock_isfile,
        mock_parse_args
    ):
        """
        Test que testeja tot el main amb fitxer.
        
        Args:
             mock_exit: 
             mock_ex4: 
             mock_ex3: 
             mock_ex2: 
             mock_ex1: 
             mock_exists: 
             mock_isfile: 
             mock_parse_args: 
        """
        mock_parse_args.return_value = MagicMock(ex=None, file="data.xlsx")
        mock_ex1.return_value = "df_read"
        mock_ex2.return_value = "merged_df"

        main()

        mock_ex1.assert_called_once_with("data.xlsx")
        mock_ex2.assert_called_once_with("df_read")
        mock_ex3.assert_called_once_with("merged_df")
        mock_ex4.assert_called_once_with("merged_df")
        mock_exit.assert_called_once_with(0)
