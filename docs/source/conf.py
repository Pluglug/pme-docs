# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Pie Menu Editor'
copyright = '2024, Pluglug and contributors'
author = 'Pluglug and contributors'
release = '1.18.8'
master_doc = 'index'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    # 'sphinx_autodoc_typehints'
    # 'sphinx.ext.autosectionlabel',
    # 'sphinxcontrib.menuselection',
]

templates_path = ['_templates']
exclude_patterns = []

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'bpy': ('https://docs.blender.org/api/current', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_css_files = ['css/custom.css']

# html_theme = 'sphinx_book_theme'

# html_theme = 'furo'
# html_title = "Pie Menu Editor"
# html_theme_options = {
#     'default_mode': 'light',
# }

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': False,
    # 'prev_next_buttons_location': 'both',
    'style_external_links': True,
    'style_nav_header_background': '#0d82d0',
    'collapse_navigation': True,
    'sticky_navigation': False,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# def setup(app):
#     app.add_css_file('custom.css')
