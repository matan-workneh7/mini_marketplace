import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Import and setup Django
import django
django.setup()

# Import the WSGI application after Django is set up
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
