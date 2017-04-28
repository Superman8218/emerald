#settings/local.py

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'emerald',
        'USER': 'zac',
        'PASSWORD': 'confidence',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'debug_log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/debug.log',
        },
        'info_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/info.log',
        },
        'error_log': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['debug_log'],
            'level': 'DEBUG',
            'propogate': True,
        },
    'importer': {
        'handlers': ['info_log', 'error_log'],
        'level': 'DEBUG',
        'propogate': False,
        },
    },
}

ALLOWED_HOSTS = ['127.0.0.1']

# Mailtrap.io
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'ff5bf54286842f'
EMAIL_HOST_PASSWORD = '0fe4318692fdfa'
EMAIL_PORT = '2525'
