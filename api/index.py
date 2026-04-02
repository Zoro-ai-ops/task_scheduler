# api/index.py is required for vercel deployments to work correctly.
# It imports the app instance from the main application file (app.py)
# and makes it available for Vercel to run the application.

from app import app