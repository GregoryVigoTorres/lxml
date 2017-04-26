#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import lxml_rtd_sphinx_theme

# sys.path manipulation
# lxml must be built inplace
# for relative imports and API/Test to work
# i.e. the .so files need to be in lxml/src dir

ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

LXML_DIR = os.path.join(ROOT, 'src')
assert os.path.exists(LXML_DIR)
sys.path.insert(0, LXML_DIR)

# -- General configuration ------------------------------------------------
extensions = ['sphinx.ext.ifconfig', 'sphinx.ext.autodoc']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = 'lxml'
copyright = '2017, lxml project'
author = 'lxml project'

# The short X.Y version.
version = '3.7'
# The full version, including alpha/beta/rc tags.
release = '3.7.2'

language = None
exclude_patterns = []
pygments_style = 'sphinx'

todo_include_todos = False

# -- Options for HTML output ----------------------------------------------
html_theme = 'lxml_rtd_sphinx_theme'
# html_style = 'css/lxml_theme.css'
html_split_index = True

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'lxmldoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'lxml.tex', 'lxml Documentation',
     'lxml project', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'lxml', 'lxml Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'lxml', 'lxml Documentation',
     author, 'lxml', 'One line description of project.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


