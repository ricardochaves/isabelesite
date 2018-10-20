import os

from google.oauth2 import service_account

S_DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_DATA_BASE"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "TEST": {"NAME": "mytestdatabase"},
    }
}

S_DEBUG = True

S_ALLOWED_HOSTS = ["*"]

S_GS_CREDENTIALS = service_account.Credentials.from_service_account_file("./SiteIsabele-0cf6ea54da5e.json")
