"""
WSGI config for licitafacil project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from dotenv import read_dotenv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'licitafacil.settings')
read_dotenv()
application = get_wsgi_application()
