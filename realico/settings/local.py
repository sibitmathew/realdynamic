from .base import *  # pylint: disable=unused-wildcard-import  # NOQA


DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

CORS_ORIGIN_ALLOW_ALL = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'USER': os.environ.get('PGUSER', 'postgres'),
#         'PASSWORD': os.environ.get('PGPASSWORD', 'dev-password'),
#         'NAME': os.environ.get('PGDB', 'dev-database'),
#         'HOST': os.environ.get('PGHOST', 'db'),
#         'PORT': os.environ.get('PGPORT', '5432')
#     }
# }
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, '..', 'static'))
MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, '..', 'media'))
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'api.request.logger': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
    },
}

# XDomain configuration
XDOMAIN_ORIGIN_REGEX = 'http://*'

# Django debug toolbar for local development
# INSTALLED_APPS.extend([
#     'debug_toolbar',
# ])

# MIDDLEWARE.extend(
#     [
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
#     ]
# )

# # Forces django toolbar to show in case you are running in docker
# def show_toolbar(request):
#     return True

# DEBUG_TOOLBAR_CONFIG = {
#     "SHOW_TOOLBAR_CALLBACK": show_toolbar,
# }