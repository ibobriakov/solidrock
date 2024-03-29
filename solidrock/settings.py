# -*- coding: utf-8 -*-
# Global settings for solidrock project.

from os.path import abspath, dirname, basename, join, split
from datetime import timedelta


MAIN_APPS_PATH = abspath(dirname(__file__))
MAIN_APPS_NAME = basename(MAIN_APPS_PATH)
PROJECT_PATH = split(MAIN_APPS_PATH)[0]
PROJECT_NAME = basename(PROJECT_PATH)

FILE_UPLOAD_PERMISSIONS = 0o644

AUTO_RENDER_SELECT2_STATICS = False

THUMBNAIL_FORMAT = "PNG"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {}

TIME_ZONE = 'Asia/Krasnoyarsk'
LANGUAGE_CODE = 'EN-en'
USE_I18N = True
USE_L10N = True
LOGIN_URL = '/#login'

STATIC_ROOT = join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL
MEDIA_ROOT = join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
STATICFILES_DIRS = ()
TEMPLATE_DIRS = ()

FIXTURE_DIRS = (
    join(PROJECT_PATH, 'dynamic_paper', 'fixtures')
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

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
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'main.backends.EmailWithPermissionBackend'
)

ANONYMOUS_USER_ID = -1
SITE_ID = 1
SECRET_KEY = '#mu+(#^z@t#q4=06!uvslz*amvj18!kjrzxq)t2&ue_99g8a2v'
ROOT_URLCONF = 'solidrock.urls'
WSGI_APPLICATION = 'solidrock.wsgi.application'


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    'main.context_processors.url_name'
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.flatpages',

    'registration',
    'south',
    'mptt',
    'tastypie',
    'gunicorn',
    'djcelery',
    'sorl.thumbnail',
    'constance',
    'constance.backends.database',
    'flatblocks',
    'redactor',
    'haystack',
    'widget_tweaks',
    "djcelery_email",
)

LOCAL_APPS = (
    'main',
    'dynamic_paper',
    'resume',
    'cover_letter',
    'registration_rest_backend',
    'userprofile',
    'job_seeker',
    'employer',
    'search',
    'promo',
    'contactus',
    'payment',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CONSTANCE_CONFIG = {
    'DEFAULT_AVATAR': ('/static/main/img/avatar_test.jpg', 'Default avatar url'),
    'DEFAULT_COMPANY_LOGO': ('/static/main/img/avatar_test.jpg', 'Default avatar url'),
}

for item in LOCAL_APPS:
    INSTALLED_APPS += (item,)
    TEMPLATE_DIRS += (join(PROJECT_PATH, item, 'templates'),)
    STATICFILES_DIRS += ((item, join(PROJECT_PATH, item, 'static')),)

#Django-registration settings
ACCOUNT_ACTIVATION_DAYS = 7

#celery url
BROKER_URL = 'amqp://guest:guest@localhost:5672/'

CELERYBEAT_SCHEDULE = {
    'rotate-jobs': {
        'task': 'employer.tasks.rotate_jobs',
        'schedule': timedelta(hours=1),
    },
}


FLATBLOCKS_AUTOCREATE_STATIC_BLOCKS = True

HAYSTACK_CONNECTIONS = {  # Should be changed at production
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

SOUTH_MIGRATION_MODULES = {
    'auth': 'userprofile.auth_migrations',
}

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

from local import *

import djcelery
djcelery.setup_loader()
