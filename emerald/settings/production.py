from .base import *

# THIS IS ONLY TEMPORARY!!!
DEBUG = True

ALLOWED_HOSTS = ['www.emeraldgov.com']

#SendGrid settings

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_API_KEY']
EMAIL_PORT = '25'

# Restrict access until push to production
# ROOT_URLCONF = 'emerald.urls_landing_only'
