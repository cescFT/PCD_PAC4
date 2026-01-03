# Pràctica d'Evaluació Contínua 4: Programació per a la ciència de dades

Francesc Ferré Tarrés

Màster Universitari en Ciències de Dades

# Estructures de les carpetes

# Desenvolupament del projecte

primer cop per crear l'entorn virtual:
* virtualenv venv

per accedir a l'entorn:
* .\venv\Scripts\activate.ps1

instal·lar requeriments: pip install -r requirements.txt

per desactivar l'entorn:
* deactivate

per executar: python -m src.execution.main


## Execució dels tests en l'entorn virtual


## Càlcul del coverage

## Generar documentació en HTML a partir del docstring

## Revisar que es compleix PEP8



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

# Exportar projecte usant setup.py

a l'arrel del projecte: pip install .

generara un executable PCD_PAC4-cli, el qual es pot executar per terminal.

(revisar a l'enunciat si falta alguna cosa més a documentar)

TODOs: Afegir referencies al codi :)