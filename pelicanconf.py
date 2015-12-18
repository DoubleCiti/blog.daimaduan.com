#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'DoubleCiti'
SITENAME = u'\u4ee3\u7801\u6bb5\u535a\u5ba2'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

LOCALE = ['zh_CN.UTF-8']
DEFAULT_LANG = 'zh'

THEME = 'theme'
BOOTSTRAP_THEME = 'lumen'
DISPLAY_CATEGORIES_ON_MENU = False
FAVICON = 'theme/favicon.ico'
# DISQUS_SITENAME = 'daimaduan-blog'
# DISQUS_NO_ID = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('回到代码段', 'http://daimaduan.com/'),
         ('项目主页', 'https://github.com/DoubleCiti/daimaduan.com'),
         ('我有建议', 'https://github.com/DoubleCiti/daimaduan.com/issues/new'))

DEFAULT_PAGINATION = 10

# URI settings
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
