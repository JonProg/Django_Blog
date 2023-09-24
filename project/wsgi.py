"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

#DOTENV
load_dotenv(BASE_DIR / 'dotenv_files' / '.env', override=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()

app = application
