# -*- coding: utf-8 -*-

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'bdd_dev',
    }
}

SECRET_KEY = "development"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# endroit ou ce sera stocké sur le serveur
STATIC_ROOT = os.path.join(ENV_DIR, 'deploy/static/')
# url à laquelle elle sera servie : www.ascenseur-en-copropriete.com/static/
STATIC_URL = '/static/'
# endroit où les fichier statiques sont avant collectstatic, avant d'être dans static root
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "ascenseur/static"),
]

MEDIA_ROOT = os.path.join(ENV_DIR, 'deploy/media/')
MEDIA_URL = '/media/'