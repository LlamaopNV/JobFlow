# app/__init__.py
import os
from flask import Flask
from app.models import db
from app.routes import main_bp
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ensure the upload folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Initialize the database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register routes blueprint
    app.register_blueprint(main_bp)

    return app
