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

# Taking the .html out of all URLs
ARTICLE_URL = '{slug}'
PAGE_URL = '{slug}'
ARTICLE_LANG_URL = '{slug}-{lang}'
DRAFT_URL = 'drafts/{slug}'
DRAFT_LANG_URL = 'drafts/{slug}-{lang}'
PAGE_URL = 'pages/{slug}'
PAGE_LANG_URL = 'pages/{slug}-{lang}'
DRAFT_PAGE_URL = 'drafts/pages/{slug}'
DRAFT_PAGE_LANG_URL = 'drafts/pages/{slug}-{lang}'
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

# The first part of the tuple should be the name of the icon
# you want from this list: https://forkaweso.me/Fork-Awesome/icons/
SOCIAL = (('youtube-play', 'https://www.youtube.com/@tian_creator'),
          ('instagram', 'https://www.instagram.com/tian_creator'),
          ('linkedin', 'https://linkedin.com/in/tian-lin-mit'),)

PROFILE_IMAGE = 'avatar.jpg'

MENUITEMS = (('Home', '/'),)
