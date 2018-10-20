"""
WSGI config for base_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base_site.settings")

application = get_wsgi_application()

application = WhiteNoise(application, root="/var/www/isabele/static/", max_age=31536000)
application.add_files("/var/www/isabele/media/", prefix="media/")
