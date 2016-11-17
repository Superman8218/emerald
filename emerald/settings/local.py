#settings/local.py

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'emerald',
        'USER': 'zac',
        'PASSWORD': 'confidence',
        'HOST': 'localhost',
        'PORT': '',
    }
}
