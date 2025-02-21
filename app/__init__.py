import os
from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Ensure upload folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    app.register_blueprint(main)

    return app