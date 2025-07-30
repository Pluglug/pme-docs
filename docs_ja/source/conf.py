# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Pie Menu Editor (日本語)"
copyright = "2024, Pluglug and contributors"
author = "Pluglug and contributors"
release = "1.18.8"
master_doc = "index"

# Language settings
language = "ja"
html_language = "ja"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",  # Load myst_parser first
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",  # Support for NumPy and Google style docstrings
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx_design",
    # 'sphinx_autodoc_typehints'
    # 'sphinx.ext.autosectionlabel',
    # 'sphinxcontrib.menuselection',
]

templates_path = ["_templates"]
exclude_patterns = []

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "bpy": ("https://docs.blender.org/api/current", None),
}

# -- Options for MyST parser ------------------------------------------------
source_suffix = [".rst", ".md"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    # 'linkify',  # Temporarily disabled due to dependency issues
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

html_theme = "furo"

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#0d82d0",
        "color-brand-content": "#0d82d0",
    },
    "dark_css_variables": {
        "color-brand-primary": "#4CAF50",
        "color-brand-content": "#4CAF50",
    },
}

html_title = "PME ドキュメント"

def setup(app):
    app.add_css_file("css/custom.css")
