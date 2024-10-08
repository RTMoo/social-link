# General settings that are used in all environments (development, testing, production).

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(dotenv_path=BASE_DIR / '.env')

ROOT_URLCONF = "main.urls"

INTERNAL_IPS = [
    "127.0.0.1",
]

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
AUTH_USER_MODEL = "accounts.CustomUser"
