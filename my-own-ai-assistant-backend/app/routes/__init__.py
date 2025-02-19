from flask import Blueprint

# Create a blueprint for the routes
routes_blueprint = Blueprint('routes', __name__)

# Import route handlers here
from . import example_routes  # Replace with actual route files as needed

# Register the blueprint in the main application file
# This can be done in app/main.py using:
# app.register_blueprint(routes_blueprint)