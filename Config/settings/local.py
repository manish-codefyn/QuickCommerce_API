from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.sqlite3',  # Use SQLite
     'NAME': BASE_DIR / 'db.sqlite3',        # Database file location
    }
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debug Toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1']

# CORS for development
CORS_ALLOW_ALL_ORIGINS = True