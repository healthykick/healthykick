#!/usr/bin/python3
#
import os
import sys

sys.path.append("/usr/local/lib/python3.4/dist-packages/")
sys.path.append("/var/www/html/healthykick/healthykick")

os.environ["DJANGO_SETTINGS_MODULE"] = "healthykick.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()