from .base import *

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'polls_db',
        'USER': 'root',
        'PASSWORD': 'hidetoshi0424',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

STATIC_URL = '/static/'
