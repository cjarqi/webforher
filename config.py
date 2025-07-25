# config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a-very-secret-key-for-dev')



    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'cjarqi')
    DB_NAME = os.environ.get('DB_NAME', 'gift_website')
    DB_PORT = os.environ.get('DB_PORT', '3306')