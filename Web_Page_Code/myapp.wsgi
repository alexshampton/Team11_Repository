import sys
import os
import logging

# Setup logging
logging.basicConfig(filename='/var/log/apache2/flaskapp_wsgi.log', level=logging.DEBUG)

try:
    # Adjust this path to your project's path
    sys.path.insert(0, '/home/jberg2021/Team11_Repository/Web_Page_Code')
    
    # Import your Flask app
    from main import app as application  # Ensure your Flask app is named `app`
    
    logging.info("WSGI application loaded successfully.")
except Exception as e:
    logging.error("Error loading WSGI application: %s", e)

