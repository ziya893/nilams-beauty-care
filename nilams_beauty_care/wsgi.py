"""
WSGI config for nilams_beauty_care project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nilams_beauty_care.settings')

application = get_wsgi_application()
