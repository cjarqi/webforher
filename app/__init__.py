# app/__init__.py

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object globally
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static')
    
    # Load all configurations from config.py
    app.config.from_object(config_class)

    # Debugging print statement
    print("--- DATABASE CONNECTION DETAILS ---")
    print(f"URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print("-----------------------------------")

    # Initialize the db extension with the app
    db.init_app(app)

    # --- Register Blueprints ---
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app