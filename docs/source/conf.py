# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Pie Menu Editor Fork'
copyright = '2024, Pluglug and contributors'
author = 'Pluglug and contributors'
release = '0.1'
# master_doc = 'getting_started'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',
    # 'sphinx_autodoc_typehints'
]


templates_path = ['_templates']
exclude_patterns = []


intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'bpy': ('https://docs.blender.org/api/current', None),
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
