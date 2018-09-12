import os

DATABASES = {
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
# DATABASES = {
#     "default": {"ENGINE": "django.db.backends.mysql", "OPTIONS": {"read_default_file": "/var/www/isabele/my.cnf"}}
# }
