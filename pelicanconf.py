#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alex Nguyen'
SITENAME = 'Alex\'s Home page'
SITETITLE = AUTHOR
SITESUBTITLE = '<pre>programming blog to document ... stuff</pre>'
# relative filepaths to: https://github.com/alexandrevicenzi/Flex/tree/master && https://github.com/getpelican/pelican-plugins/
THEME = "../blog-resources/Flex"
PLUGIN_PATHS = ['../blog-resources/pelican-plugins/']
PLUGINS = ['better_codeblock_line_numbering', 'bootstrapify', 'pelican_javascript', 'pdf-img']
# Theme Settings
SITELOGO = '/images/profile.jpg'
PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Main Menu
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (('Archives', '/archives'),('Categories', '/categories'),('Tags', '/tags'),)

# Blogroll (add ('title', '/relative/path') tuple for left side pane links)
LINKS = ()

# Social widget
SOCIAL = (
    ('github', 'https://github.com/alexnguyennn'),
    ('linkedin', 'https://www.linkedin.com/in/alex-nguyen-8927b966/'))

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'pdfs']
ARTICLE_URL = 'blog/{date:%Y}/{slug}'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# Formatting for URLS
PAGE_URL = 'pages/{slug}'
CATEGORY_URL = 'category/{slug}'
TAG_URL = 'tag/{slug}'
