#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alex Nguyen'
SITENAME = 'Alex\'s Home page'
SITEURL = ''
THEME = "../pelican-themes/Flex"
PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['better_codeblock_line_numbering', 'bootstrapify', 'pelican_javascript']

PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Gradlink Presentation', '/gradwikipresentation'),
         ('Misc Projects', 'https://github.com/AlexN34/misc'))

# Social widget
SOCIAL = (('Github', 'github.com/alexn34'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
