from flask import Flask, request, jsonify
from app.routes import main_routes

def create_app():
    app = Flask(__name__)
    
    app.config['JSON_SORT_KEYS'] = False  # Optional: Prevents sorting of JSON keys

    # Register routes
    app.register_blueprint(main_routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)