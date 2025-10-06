import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'Fasta Project'
copyright = '2024, Fasta Project Team'
author = 'Fasta Project Team'

release = '0.1.0'
version = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    'style_nav_header_background': '#1e6fb8',
    'collapse_navigation': False,
    'sticky_navigation': True,
}

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

def setup(app):
    app.add_css_file('custom.css')
