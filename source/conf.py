# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Space Information Dynamics Group'
copyright = '2024, Purdue Space Information Dynamics Group'
author = 'Liam Robinson'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_design",
    "sphinxcontrib.bibtex",
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_favicon = "_static/sid_logo_dark.ico"
html_theme_options = { 
        "logo": {
        "image_light": "_static/sid_logo_light.png",
        "image_dark": "_static/sid_logo_dark.png",
        "text": "SID Group",
        "nosidebar": True,
    },
  "footer_start": ["copyright"],
  "footer_end": [],
  "secondary_sidebar_items": [],
  "show_prev_next": False,
}
html_show_sourcelink = False
html_show_sphinx = False
html_permalinks = False

import os
bibtex_bibfiles = [os.path.join("_static/bib", x) for x in os.listdir("_static/bib") if x.endswith(".bib")]

import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
