from .base import *  # noqa

print("Local Tenants")

# Application definition

BASE_APPS = [
    "django_tenants",
    "organizations",
]

THIRD_PARTY_APPS += ["django_extensions"]  # noqa F405

SHARED_APPS = BASE_APPS + DJANGO_APPS + THIRD_PARTY_APPS

INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

# Compressor Cache Middleware

CACHE_MIDDLEWARE = []

# Tenants Middleware

TENANTS_MIDDLEWARE = ["django_tenants.middleware.main.TenantMainMiddleware",]

MIDDLEWARE = TENANTS_MIDDLEWARE + MIDDLEWARE + CACHE_MIDDLEWARE

# Tenats
# https://django-tenants.readthedocs.io/en/latest/index.html

TENANT_MODEL = "organizations.Organization"

TENANT_DOMAIN_MODEL = "organizations.Domain"

ROOT_URLCONF = "core.urls_tenants"
PUBLIC_SCHEMA_URLCONF = "core.urls_public"

# CACHES = {
#     "default": {
#         "KEY_FUNCTION": "django_tenants.cache.make_key",
#         "REVERSE_KEY_FUNCTION": "django_tenants.cache.reverse_key",
#         "BACKEND": "django.core.cache.backends.db.DatabaseCache",
#         "LOCATION": "schedule_cache",
#     },
# }

# Database Settings

DB_POSTGRESQL_ENGINES = "django_tenants.postgresql_backend"

db_config["ENGINE"] = DB_POSTGRESQL_ENGINES

DATABASES = {
    "default": db_config,
}

DATABASE_ROUTERS = ("django_tenants.routers.TenantSyncRouter",)

# Django Extensions
# https://django-extensions.readthedocs.io/en/latest/index.html
DJANGO_EXTENSIONS_RESET_DB_POSTGRESQL_ENGINES = DB_POSTGRESQL_ENGINES
