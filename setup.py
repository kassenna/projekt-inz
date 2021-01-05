import os
from setuptools import setup
from nvpy import nvpy

setup(
    name="Przepis na matematykę",
    version="1.0",
    author="Katarzyna Majgier",
    author_email="katamaj392@student.polsl.pl",
    description="Demo of packaging a Python script as DEB",
    license="BSD",
    url="https://github.com/kassenna/Projekt-inz",
    packages=['Gra w sklep'],
    entry_points={
        'console_scripts': ['myscript = myscript.myscript:main']
    },
    data_files=[
        ('share/applications/', ['vxlabs-myscript.desktop'])
    ], install_requires=['pygameAssets', 'pygame', 'tinydb']

)
