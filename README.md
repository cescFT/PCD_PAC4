# Pràctica d'Evaluació Contínua 4: Programació per a la ciència de dades

Francesc Ferré Tarrés

Màster Universitari en Ciències de Dades

WIP

primer cop per crear l'entorn virtual:
* virtualenv venv

per accedir a l'entorn:
* .\venv\Scripts\activate.ps1

per desactivar l'entorn:
* deactivate

per executar tests:
* python -m tests.suite

pel coverage:
* he instal·lat coverage -> pip install coverage
* coverage run -m tests.suite
* coverage report
* coverage html <- fa un html bonic

per executar el main: python -m src.main

pel doc:
* pip install pydoctor
* pydoctor --make-html --project-name "PCD_PAC4 - Francesc Ferré Tarrés" --html-output doc src/


estandard PEP8:
* pip install pylint
* pylint src/
* Per generar el ignore: pylint --generate-rcfile | Out-File -Encoding utf8 .pylintrc



