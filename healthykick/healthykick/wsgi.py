"""
WSGI config for tandel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/var/www/django/healthykick')
os.environ['DJANGO_SETTINGS_MODULE'] = 'healthykick.settings'

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tandel.settings")

application = get_wsgi_application()
