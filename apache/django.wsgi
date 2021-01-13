import os
import sys
 
path = 'C:\AppServ\www\Project'
if path not in sys.path:
    sys.path.insert(0, 'C:\AppServ\www\Project')
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'Project.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()