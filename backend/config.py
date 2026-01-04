import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    DEBUG = True

    # Database
    DATABASE_PATH = os.path.join(BASE_DIR, "blue_carbon.db")

    # Uploads
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    ALLOWED_EXTENSIONS = {"csv"}

    # Security
    SECRET_KEY = "blue-carbon-secret-key"
