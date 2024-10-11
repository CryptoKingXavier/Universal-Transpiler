from os import makedirs
from os.path import exists
from secrets import token_hex


# Configure upload folder
UPLOAD_FOLDER = "./database"
makedirs(UPLOAD_FOLDER) if not exists(UPLOAD_FOLDER) else None


# Allowed file extensions
ALLOWED_EXTENSIONS = ["java", "py"]


class Config:
    SECRET_KEY = token_hex(16)
    UPLOAD_FOLDER = UPLOAD_FOLDER
