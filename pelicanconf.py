import os
import sys
sys.path.append(os.curdir)

from markdown_custom import TianExtension

MARKDOWN = {
  'extensions': [TianExtension()],
  'extension_configs': {
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}


AUTHOR = 'Tian Lin'
SITENAME = 'Tian Lin'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = False
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Overriding index page
INDEX_SAVE_AS = 'posts.html'

# Taking the .html out of all URLs
ARTICLE_URL = '{slug}'
ARTICLE_LANG_URL = '{slug}-{lang}'

PAGE_URL = '{slug}'
PAGE_LANG_URL = '{slug}-{lang}'
PAGE_SAVE_AS = '{slug}.html'

DRAFT_URL = 'drafts/{slug}'
DRAFT_LANG_URL = 'drafts/{slug}-{lang}'

DRAFT_PAGE_URL = 'drafts/{slug}'
DRAFT_PAGE_LANG_URL = 'drafts/{slug}-{lang}'

AUTHOR_URL = 'author/{slug}'
CATEGORY_URL = 'category/{slug}'
TAG_URL = 'tag/{slug}'

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# If you don't set a summary, this is how many words
# from the start will be automatically turned into one.
SUMMARY_MAX_LENGTH = 0

# Customization
THEME = 'themes/pelican-hyde'
COLOR_THEME = '07'
TEMPLATE_PAGES = {
    "home.html": "index.html"
}

# The first part of the tuple should be the name of the icon
# you want from this list: https://forkaweso.me/Fork-Awesome/icons/
SOCIAL = (('youtube-play', 'https://www.youtube.com/@tian_creator'),
          ('instagram', 'https://www.instagram.com/tianlifey'),
          ('linkedin', 'https://linkedin.com/in/tian-lin-mit'),)

PROFILE_IMAGE = 'avatar.jpg'

MENUITEMS = (
    ('Home', ''),
    ('About', 'about'),
    ('Posts', 'posts'),
)


FRONT_PAGE_TAGS = {
    "travel": {
        "title": "Travel",
        "thumbnail": "compass.webp"
    },
    "theater": {
        "title": "Theater",
        "thumbnail": "masks.webp"
    },
    "review": {
        "title": "Reviews",
        "thumbnail": "quill.webp"
    },
}

