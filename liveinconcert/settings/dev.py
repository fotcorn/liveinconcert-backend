from .base import *

DEBUG = True

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

# log ./mange.py runserver requests
LOGGING['loggers']['django.server'] = {
    'handlers': ['console'],
    'level': 'INFO',
    'propagate': False,
}

LOGGING['loggers']['django.db.backends'] = {
    'handlers': ['console'],
    'level': 'ERROR',  # change this to DEBUG to log executed SQL statements
    'propagate': False,
}
