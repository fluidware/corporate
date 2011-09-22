import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Chide.it', 'developers@chide.it'),
)

ROOT = os.path.dirname(os.path.realpath(__file__))

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False
USE_L10N = False

MEDIA_ROOT = '%s/media/' % ROOT
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin/media/'

SECRET_KEY = 'thisisasecret'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'chide.urls'

TEMPLATE_DIRS = (
    '%s/templates/' % ROOT,
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
)

try:
	from settings_local import *
except ImportError:
	pass
