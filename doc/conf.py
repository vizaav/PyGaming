# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys


print(sys.path)

sys.path.insert(0, os.path.abspath('..'))

project = 'BrajanekDefence'
copyright = '2023, Izabela Pawlukowska'
author = 'Izabela Pawlukowska'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['rinoh.frontend.sphinx', 'sphinx.ext.autodoc', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_theme_options = {
    'description': 'Dokumentacja projektu PyGaming',
    'fixed_sidebar': True,
    'formats': ['html', 'pdf']
}

latex_engine = 'pdflatex'
latex_documents = [
    ('index', 'documentacja.tex', 'Dokumentacja projektu PyGaming',
     'Twórca dokumentacji', 'manual'),
]

# -- Options for rinoh output ------------------------------------------------

rinoh_documents = [
    ('index',              # top-level file (index.rst)
        'documentacja',       # output (target.pdf)
        'Dokumentacja projektu PyGaming',   # document title
        'Twórca dokumentacji: Filip Król Izabela Pwalukowska')    # document author
]