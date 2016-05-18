"""
WSGI config for emerald project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

# Add to python path
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))



from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emerald.settings")

application = get_wsgi_application()
