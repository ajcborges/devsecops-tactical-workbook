# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

# General information about the project.
project = u'DevSecOps Quickstart'
copyright = u'Copyright © 2020 by Franklin Diaz'
author = u'© 2020 by Franklin Diaz'

# The short X.Y version
version = '0.0.3'
# The full version, including alpha/beta/rc tags
# this will show on title page if uncommented
#release = '0.0.1'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.graphviz',
    'rst2pdf.pdfbuilder']

# Turns on numbered figures for HTML output
numfig = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'colorful'

show_authors = True


# -- Options for HTML output -------------------------------------------------
# The Read the Docs theme is available from
# - https://github.com/snide/sphinx_rtd_theme
# - https://pypi.python.org/pypi/sphinx_rtd_theme
# - python-sphinx-rtd-theme package (on Debian)
try:
    #import sphinx_rtd_theme
    #html_theme = 'sphinx_rtd_theme'
    #html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_theme = 'theme' # use the theme in subdir 'theme'
    html_theme_path = ['.'] # make sphinx search for themes in current dir
except ImportError:
    sys.stderr.write('Warning: The Sphinx custom HTML theme was not found. Falling back to the default theme.\n')
    #sys.stderr.write('Warning: The Sphinx \'sphinx_rtd_theme\' HTML theme was not found. Make sure you have the theme installed to produce pretty HTML output. Falling back to the default theme.\n')

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # Disable showing the sidebar. Defaults to 'false'
    'nosidebar': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['theme/static']
html_context = {
    'css_files': [
        'theme/static/colorful.css',
    ],
}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
html_sidebars = {}

html_use_index = False
html_show_sphinx = False
html_domain_indices = False

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
#latex_documents = [(master_doc, 'calibre.tex', title, 'Franklin Diaz', 'manual', False)]

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True

#latex_elements = { 'maketitle': copyright,
# 'extraclassoptions': 'openany,oneside' }
# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'images/plouzane-1758197_1920.jpg'
latex_show_pagerefs = True
latex_show_urls = 'footnote'
#latex_additional_files = ['sphinxmanual.cls']
#latex_additional_files = ['copyrights.cls']
latex_elements = {
    'inputenc': '',
    'utf8extra': '',
    'papersize':'letterpaper',
    #'fontenc':r'\usepackage[T2A,T1]{fontenc}',
    'preamble': r'\input{../../_static/mypreamble.tex}',
    'maketitle': r'\input{../../_static/maketitle.tex}',
    'footer': r'''
      \small \textit{Follow along code project available from }{\href{https://github.com/hotpeppersec/rapid_secdev_framework}{RapidSecDevFramework}}
    ''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'sphinxsetup': \
        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        HeaderFamily=\\rmfamily\\bfseries, \
        InnerLinkColor={rgb}{0,0,1}, \
        OuterLinkColor={rgb}{0,0,1}',

        'tableofcontents':' ',
}

# -- Options for PDF output --------------------------------------------------
#pdf_documents = [('index', 'documentation', My Docs', 'Me'), ]

# -- Options for EPUB output -------------------------------------------------

epub_theme = 'theme'
#epub_version = u'3.0'
epub_basename = 'DevSecOpsQuickStart'
epub_title = u'DevSecOps Quickstart'
epub_author = 'Franklin Diaz'
epub_copyright = u'© 2020 by Franklin Diaz'
epub_publisher = 'http://sphinx-doc.org/'
# A unique identification for the text.
epub_uid = 'web-site'
# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = 'url'
# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = epub_publisher
# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = [('index.xhtml', 'Welcome')]
# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = [('usage/installation.xhtml', 'Installing Sphinx'), ('develop.xhtml', 'Sphinx development')]

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['_source/global.rst',
                      '_source/x2_heroku.rst',
                      '_source/x3_ruby.rst', 
                      '_source/x1_extras.rst',
                      '_source/x4_resources.rst',
                      '_source/x5_scanners.rst'
                      ]
epub_fix_images = False
epub_max_image_width = 0
epub_show_urls = 'inline'
epub_use_index = False
#epub_guide = (('toc', 'contents.xhtml', 'Table of Contents'),)
epub_description = 'A workbook to get you started with secure development.'

# A tuple containing the cover image and cover page html template filenames.
epub_cover = ('', 'epub-cover.html')
# The depth of the table of contents in toc.ncx.
epub_tocdepth = 3
# Allow duplicate toc entries.
epub_tocdup = False

# -- Options for Mobi output ---------------------------------------------------

mobi_theme = "mobi"
mobi_title = u'DevSecOps Quickstart'
mobi_author = u'Franklin Diaz'
mobi_publisher = u'Franklin Diaz'
mobi_copyright = u'© 2020 by Franklin Diaz'

# The scheme of the identifier. Typical schemes are ISBN or URL.
#mobi_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#mobi_identifier = ''

# A unique identification for the text.
#mobi_uid = ''

#mobi_cover = "_static/cover.png"

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#mobi_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#mobi_post_files = []

# A list of files that should not be packed into the mobi file.
mobi_exclude_files = ['_static/opensearch.xml', '_static/doctools.js',
    '_static/jquery.js', '_static/searchtools.js', '_static/underscore.js',
    '_static/basic.css', 'search.html', '_static/websupport.js']

# The depth of the table of contents in toc.ncx.
mobi_tocdepth = 2

# Allow duplicate toc entries.
mobi_tocdup = False

mobi_add_visible_links = False
