import os
import sys
import django
from django.core.wsgi import get_wsgi_application

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

application = get_wsgi_application()
