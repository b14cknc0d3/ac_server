import os
import sys
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application



sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'anchorage_consultancy.settings'
application = get_wsgi_application()