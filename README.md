# Pràctica d'Evaluació Contínua 4: Programació per a la ciència de dades

Francesc Ferré Tarrés

Màster Universitari en Ciències de Dades

# Estructures de les carpetes i fitxers

* **data/**: Conté els fitxers de la PAC4 a ser processats.
* **doc/**: Conté la documentació creada a través dels *docstrings* del codi.
* **screenshots/**: Conté les captures de pantalla com a evidències de cada apartat.
* **src/**: Conté els paquets creats per a solucionar la pràctica.
    * **src/execution/**: Conté el `main.py` el qual permet passar-li arguments, tal com s'anomena en l'enunciat.
    * **src/img/**: Conté la imatge del gràfic creat com a resposta en l'exercici 3. Si no està creada la carpeta,
    el codi la crearà.
    * **src/modules/exercises**: Conté subpaquets, un per cada exercici, a més dels mòduls auxiliars creats per a donar
    resposta a l'exercici corresponent.
    * **src/report/**: Conté el JSON creat com a resposta de l'exercici 4. Si no existeix, el codi la crearà, jutament
    amb el JSON.
* **tests/**: Conté subpaquets, un per cada exercici amb cada suite i classes de test.

Finalment, en el root del projecte hi trobem els fitxers que es demanen en la PAC:
* **.pylintrc**: Permet configurar el paquet *pylint*, el qual retorna si es compleix el PEP8.
* **LICENSE**: Fitxer de llicència GPL-3.0 license.
* **README.md**: Aquest mateix fitxer, el qual dóna detalls sobre l'estructura i com executar el projecte.
* **requirements.txt**: Dependències necessàries perquè funcioni el projecte en un entorn virtual nou.
* **setup.py**: Fitxer que permet la instal·lació del projecte com a programa per la CLI.

# Desenvolupament del projecte en entorn virtual

Aquest projecte ha estat desenvolupat a través d'un entorn virtual. Per a crear un entorn virutal, cal primer instal·lar
el paquet `virtualenv`.

```shell
pip install virtualenv
```

Un cop està instal·lat aquest paquet, situeu-vos dins de la carpeta del projecte:

```shell
cd PCD_PAC4
```

*Nota: D'ara en endavant, s'assumeix que l'usuari està en aquesta carpeta.*

el que hem de fer és crear un entorn virtual, a través de la comanda:

```shell
virtualenv <nom_entorn_virtual>
```

*Nota: Substituïu `<nom_entorn_virtual>` pel nom que li volgueu donar, normalment es diu `venv`.*

Llavors, en un entorn Windows, per accedir a l'entorn, cal executar l'script següent:

```shell
.\<nom_entorn_virtual>\Scripts\activate.ps1
```

D'acord amb la documentació de la teoria, en principi en un Linux, la comanda seria:

```shell
source <nom_entorn_virtual>/bin/activate
```
*Nota: Substituïu <nom_entorn_virtual> pel nom que li heu donat a l'entorn virtual*

A continuació, instal·lem els paquets necessaris per a poder executar el projecte a través de la següent comanda:

```shell
pip install -r requirements.txt
```

Si volem executar el projecte, cal executar la següent comanda (provada en entorn Windows):

```shell
python3 -m src.execution.main
```

Hi permet el pas d'arguments, els quals són:

* **-h**: Mostra ajuda.
* **-ex <num_ex>**: El que fa és executar tots els exercici de l'1 al `<num_ex>`, atès que són exercicis progressius.
    * *Nota: Si no se li passa aquest paràmetre, per defecte, executarà tots 4 exercicis*

Finalment, si desitgem desactivar l'entorn, utilitzarem la comanda:

```shell
deactivate
```

## Execució dels tests

Per tal d'executar els tests, necessitem accedir en l'entorn virutal `<nom_entorn_virtual>`, i la comanda per
executar els tests serà:

```shell
python3 -m tests.exercise_<x>.suite_ex<x>
```

*Nota: Substituïu `<x>` per un número d'exercici vàlid (1-4)*

Per al cas del test del main:

```shell
python3 -m tests.execution.suite_main
```

## Càlcul del *Coverage* del codi

Per tal de calcular el *coverage* del codi, necessitem estar en l'entorn virtual `<nom_entorn_virtual>` el qual ja té
integrat, a través de la instal·lació del `requirements.txt` un parquet anomenat *coverage*, el qual va ser instal·lat
a través de la comanda:

```shell
pip install coverage
```

Per tal de calcular el coverage, la comanda que s'ha d'executar és:

```shell
coverage run -m tests.exercise_<x>.suite_ex<x>
coverage report
```

*Nota: Subtituïu `<x>` pel número d'exercici vàlid que volgueu saber el coverage*

Per al cas del main:

```shell
coverage run -m tests.execution.suite_main
coverage report
```

## Generar documentació en HTML a partir del *docstring*

Per tal de generar la documentació a través del *docstring*, he instal·lat en l'entorn virtual el paquet *pydoctor* a 
través de la comanda:

```shell
pip install pydoctor
```

Llavors per a generar la documentació, l'he fet amb aquesta comanda:

```shell
pydoctor --make-html --project-name "PCD_PAC4 - Francesc Ferré Tarrés" --html-output doc src tests
```

Llavors, de forma automàtica agafa tots els *docstrings* i els traspassa en varis HTML. Si es vol visualitzar, accedim a
`doc/` i veiem que hi ha un `index.html`. Si l'obrim en un navegador, observarem tota la documentació en format HTML,
tal com es demana en l'enunciat de la PAC4.

## Revisar que es compleix PEP8

Per tal de veure si es compleix el PEP8, he instal·lat el paquet *pylint*, a través de la comanda:

```shell
pip install pylint
```

*Nota: en el `requirements.txt` ja hi ha la dependència i cal estar en l'entorn virtual `<nom_entorn_virtual>` per a 
executar la revisió del PEP8.

Per tal de comprovar si es compleix, executem la comanda:

```shell
pylint src/
```

I el fitxer `.pylintrc` ha estat generat a través de la comanda (powershell de Windows):

```shell
pylint --generate-rcfile | Out-File -Encoding utf8 .pylintrc
```


# Execució projecte com a programa de CLI - Producció

Per tal d'assolir l'expertesa i un desplegament de l'aplicació creada, he generat el fitxer `setup.py`, el qual
instal·la dependències, detecta els paquets personalitzats de la pràctica i acaba generant un executable, anomenat
`PCD_PAC4-cli`.

Així doncs, per aconseguir aquest executable, executarem a l'arrel del projecte la comanda

```shell
pip install .
```

Quan aquest hagi acabat, en principi generarà l'executable `PCD_PAC4-cli`, el qual es pot executar per terminal, i que
admet els arguments `-h` i `-ex <num_ex>` anteriorment descrits.


TODOs:
* Revisar que al README estigui tot ok
* Afegir referencies al codi 
* Validar resultats
* Documentar les funcions + params entrada i sortida
* Fer tests + coverage + pep8 i captures de pantalla
* Passar les referencies al README