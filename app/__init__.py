from flask import Flask

app = Flask(__name__)

from app.routes import *

def create_app():
    return app