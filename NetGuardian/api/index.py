import sys
import os

# Make the project root importable so app.py and dashboard_module.py resolve correctly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app

# Vercel expects a callable named 'app' or 'handler'
# Flask's app object is a valid WSGI callable — this is all that's needed.
