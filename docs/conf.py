# -*- coding: utf-8 -*-
#
# Cadaques documentation build configuration file, created by
# sphinx-quickstart on Wed Mar  7 07:26:03 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import sphinx_bootstrap_theme

on_qthelp = os.environ.get('QTHELP', None) == 'True'
print('ON_QTHELP: ' + str(on_qthelp))

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('_extensions'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    'youtube',
    'issues',
    'github',
]

issues_base_url = 'https://github.com/qmlbook/qmlbook/'
github_base_url = 'https://github.com/qmlbook/qmlbook/'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Qt5 Cadaques Book'
copyright = u'2012-2018 Jürgen Bocklage-Ryannel and Johan Thelin. ' \
    'This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = os.environ.get('RELEASE_VERSION', 'local build')
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y at %H:%M CET'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.

exclude_patterns = [
    '_build', '_themes', 'unsorted',
]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# default highlighting language
highlight_language = 'qml'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# -- Options Extensions --------------------------------------------------------

# enable to output
todo_include_todos = True


extlinks = {
    'qt5': ('http://doc.qt.io/qt-5//%s.html', 'Qt5Doc '),
    'qt5r': ('http://doc.qt.io/qt-5//%s', 'Qt5Doc '),
    'qtvideo': ('http://qt-project.org/videos/watch/%s', 'QtVideo '),
}

graphviz_dot_args = [
    "-Grankdir=TB",
    "-Gfontsize=10",
    "-Gfontname=Arial",
    "-Nshape=box",
    "-Nfontsize=10",
    "-Nfontname=Arial",
    "-Ncolor=#993333",
    "-Nstyle=filled",
    "-Nfillcolor=#FFFFCC",

    "-Efontsize=10",
    "-Efontname=Arial",
    "-Ecolor=#993333",
]

# -- Options for HTML output ---------------------------------------------------


def setup(app):
    app.add_stylesheet("custom-styles.css")


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
if on_qthelp:
    html_theme = 'sphinxdoc'
else:
    html_theme = 'bootstrap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

if on_qthelp:
    html_theme_options = {}
else:
    html_theme_options = {
        'bootswatch_theme': "cosmo",
        'navbar_links': [
        ],
        'navbar_title': "QmlBook",
        'navbar_site_name': "Chapters",
    }

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = '%s v%s' % (project, version)

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = project

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = 'logo.jpg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.

# html_sidebars = {
#     'index': [],
#     'pages/*': ['localtoc.html'],
#     '*/*': ['localtoc.html'],
# }

html_sidebars = {
    'index': ['sidebar.html'],
    '*/index': ['sidebar.html'],
    'ch??-*/*': ['localtoc.html']
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'qt5cadaques'

# Prioritize gif over png for html to enable animated images
# Png is used for latex output
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg',
]


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'qt5_cadaques.tex', u'Qt5 Cadaques',
     u'JRyannel,JThelin', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = True

# If true, show URL addresses after external links.
# latex_show_urls = True

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = False


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'cadaques', u'Cadaques',
     [u'CadaquesTeam'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'Qt5 Cadaques', u'Qt5 Cadaques',
     u'JRyannel, JThelin', 'Qt5 Cadaques', 'A book about Qt5.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'


# -- Options for epub output --------------------------------------------------


epub_basename = 'qt5_cadaques'
epub_scheme = 'URL'
epub_identifier = 'qmlbook.org'
epub_publisher = 'JRyannel,JThelin'
epub_author = 'JRyannel,JThelin'
epub_title = 'Qt5 Cadaques'
epub_tocdup = False
epub_tocdepth = 2
epub_exclude_files = [
    '_static/opensearch.xml', '_static/doctools.js',
    '_static/jquery.js', '_static/searchtools.js', '_static/underscore.js',
    '_static/basic.css', 'search.html', '_static/websupport.js'
]
epub_cover = ("_static/cover.png", "epub-cover.html")
