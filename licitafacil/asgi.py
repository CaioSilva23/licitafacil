"""
ASGI config for licitafacil project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from dotenv import read_dotenv
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'licitafacil.settings')

read_dotenv()
application = get_asgi_application()
