import sys
import os

# Add the project directory to the sys.path
sys.path.insert(0, '/home/jberg2021/Team11_Repository/Web_Page_Code')

# Set the virtual environment's site-packages directory
activate_this = '/home/jberg2021/Team11_Repository/Web_Page_Code/.venv/bin/activate'
os.environ['VIRTUAL_ENV'] = '/home/jberg2021/Team11_Repository/Web_Page_Code/.venv'
os.environ['PATH'] = f"{os.environ['VIRTUAL_ENV']}/bin:" + os.environ['PATH']
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

# Import your application
from main import app as application

