# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Add documentation stored in other directories
import os
import sys
#sys.path.insert(0, r"C:\Users\Lennart\lennartGit\personal\genericmodule")
#sys.path.insert(0, os.path.abspath('./../'))
#sys.path.insert(0, os.path.abspath('..\..'))
p1 = os.path.dirname(os.path.realpath(__file__))
p2 = "..\.."
sys.path.insert(0, os.path.join(p1, p2))
#print(sys.path)
#import genericmodule.functions_a

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'genericmodule'
copyright = '2024, lg'
author = 'lg'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon']

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "nbsphinx_link"
]
napoleon_google_docstring = False
napoleon_numpy_docstring = True
# napoleon_use_param = False
# napoleon_use_ivar = True

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_static_path = ['_static']
