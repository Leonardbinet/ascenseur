import os
import sys
from django.core.wsgi import get_wsgi_application

path = '/home/yomams/ascenseur/'
path1 = '/home/yomams/ascenseur/ascenseur/'
if path not in sys.path:
    sys.path.append(path)
if path1 not in sys.path:
    sys.path.append(path1)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ascenseur.settings.production'

application = get_wsgi_application()
