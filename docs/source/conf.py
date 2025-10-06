import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

project = 'fasta pro'
copyright = '2025, Ficus-aurea'
author = 'Ficus-aurea'
release = '0.1.0'

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.viewcode',
	'sphinx.ext.autosectionlabel',
	'sphinx.ext.githubpages',
	'sphinx.ext.highlight',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'display_version': True,           # Показывать версию
    'prev_next_buttons_location': 'bottom',  # Кнопки вперед/назад внизу
    'style_external_links': True,      # Красивые внешние ссылки
    'collapse_navigation': True,       # Сворачивающаяся навигация
    'sticky_navigation': True,         # Липкая навигация
    'navigation_depth': 4,             # Глубина навигации
}
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# Фавиконка (иконка сайта)
html_favicon = '_static/favicon.ico'

# -- Дополнительные настройки ------------------------------------------------

# Автоматическая нумерация рисунков и таблиц
numfig = True

# Настройка для autosectionlabel
autosectionlabel_prefix_document = True

# Кодировка
source_encoding = 'utf-8'

# Заголовок HTML страницы
html_title = 'FASTA Pro - Документация'

