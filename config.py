# config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a-very-secret-key-for-dev')

    # --- Database Configuration ---
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'cjarqi')
    DB_NAME = os.environ.get('DB_NAME', 'gift_website')
    DB_PORT = os.environ.get('DB_PORT', '3306')

   
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    
    # Optional: silence a deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False