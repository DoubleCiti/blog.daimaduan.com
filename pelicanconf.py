#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'DoubleCiti'
SITENAME = u'\u4ee3\u7801\u6bb5\u535a\u5ba2'
SITEURL = '/'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('回到代码段', 'http://daimaduan.com/'),
         ('项目主页', 'https://github.com/DoubleCiti/daimaduan.com'),
         ('建议', 'https://github.com/DoubleCiti/daimaduan.com/issues/new'))

DEFAULT_PAGINATION = 10

# URI settings
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
