# app/__init__.py

from flask import Flask
from config import Config
import flask_mysql_connector

# Initialize the mysql object globally but without an app instance yet
mysql = flask_mysql_connector.MySQL()

def create_app(config_class=Config):
    """
    Creates and configures an instance of the Flask application.
    """
    

    app = Flask(__name__, static_folder='static')
    



    # Load configuration from the config.py file
    app.config.from_object(config_class)

    # Configure MySQL using the loaded config
    app.config['MYSQL_HOST'] = app.config['DB_HOST']
    app.config['MYSQL_USER'] = app.config['DB_USER']
    app.config['MYSQL_PASSWORD'] = app.config['DB_PASSWORD']
    app.config['MYSQL_DATABASE'] = app.config['DB_NAME']
    
    # Debugging print statement to check connection parameters
    print("--- DATABASE CONNECTION DETAILS ---")
    print(f"Host: {app.config['MYSQL_HOST']}")
    print(f"User: {app.config['MYSQL_USER']}")
    print(f"Database: {app.config['MYSQL_DATABASE']}")
    print("-----------------------------------")

    # Initialize the mysql extension with the app
    mysql.init_app(app)

    # --- Register Blueprints ---
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app