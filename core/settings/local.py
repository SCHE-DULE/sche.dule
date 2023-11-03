from .base import *  # noqa

INSTALLED_APPS += ["django_extensions"]  # noqa F405
print("Local")

# Django Extensions
# https://django-extensions.readthedocs.io/en/latest/index.html
DJANGO_EXTENSIONS_RESET_DB_POSTGRESQL_ENGINES = "django_tenants.postgresql_backend"