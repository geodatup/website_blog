#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hugo Roussaffa'
SITENAME = u'Blog'
RETOURSITEURL = 'http://geodatup.fr'
SITEURL = ''
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'
DATE_FORMATS = {
    #'en': '%a, %d %b %Y',
    'en': '%d %m %Y',
    'jp': '%Y-%m-%d(%a)',
    'fr': '%d %m %Y'}

PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code',
           'sitemap',
           #'pelican-flickr',
           ]

LOAD_CONTENT_CACHE = False

THEME = "pure-single-yo"
#EXTRA_TEMPLATES_PATHS = ['../pelican-themes/flickr/',]

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

COVER_IMG_URL = '/../../images/font2.jpg'
PROFILE_IMG_URL = 'https://fr.gravatar.com/userimage/111331765/a0bbe389f0389278de338fefc202f0e8.png?size=200'
TAGLINE = 'Geodatup'
#FAVICON_URL - Set the favicon image
DISQUS_SITENAME = "geodatup"
DISQUS_ON_PAGES = True
GOOGLE_ANALYTICS = 'UA-96092032-1'
#PIWIK_URL and PIWIK_SITE_ID - Set the URL and site-id for Piwik tracking. (Without 'http://')
MENUITEMS = (('Archives','archives.html'),)

STATIC_PATHS = ['images']

#  generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/category/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# sitemap plugin config
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

PDF_GENERATOR = False

#FLICKR_API_KEY = '51b43627304c37e85055ba4235ffe9dd'
#FLICKR_API_SECRET = '5f49bbdfc0b7e732'
#FLICKR_USER = '131609124@N08'


# Blogroll
LINKS = (('Site Web','http://geodatup.fr'),)

# Social widget
SOCIAL = (('map-marker','https://www.openstreetmap.org/node/3322982393#map=10/43.3856/2.1416'),
		  ('github-square','https://github.com/geodatup'),('rss-square',FEED_ALL_ATOM))

DEFAULT_PAGINATION = 10
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True