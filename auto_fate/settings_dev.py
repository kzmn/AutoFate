import django.conf.global_settings as defaults
import sys
#globals().update(vars(sys.modules['settings']))
from auto_fate.settings import *

# TODO: We should make a base settings file for production and have this file
# and have this file just import and modify it.  Things like the secret key
# should be common to all settings files.

# Django settings for example project.

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite3',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


