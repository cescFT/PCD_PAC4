"""

"""

from setuptools import setup, find_packages


setup(
    name="PCD_PAC4",
    version="1.0.0",
    author="Francesc Ferré Tarrés",
    description="Codi de la pràctica 4 de l'assignatura de Programació per a la Ciència de Dades",
    author_email="fferretar@uoc.edu",
    url="https://github.com/cescFT/PCD_PAC4",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "pandas",
        "matplotlib",
        "scipy",
        "openpyxl"
    ],
    entry_points={
        "console_scripts": [
            'PCD_PAC4-cli = src.execution.main:main',
        ]
    }
)