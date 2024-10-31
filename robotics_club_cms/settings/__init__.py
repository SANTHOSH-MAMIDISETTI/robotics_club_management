import os

ENVIRONMENT = os.getenv('DJANGO_ENV', 'development')

if ENVIRONMENT == 'production':
    from .production import *
else:
    from .development import *
