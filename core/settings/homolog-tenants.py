from .base import *  # noqa

print("Homolog Tenants")

# Application definition

BASE_APPS = [
    "django_tenants",
    "organizations",
]

THIRD_PARTY_APPS += ["compressor"]  # noqa F405

SHARED_APPS = BASE_APPS + DJANGO_APPS + THIRD_PARTY_APPS

INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

# Compressor Cache Middleware

CACHE_MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]

# Tenants Middleware

TENANTS_MIDDLEWARE = [
    "django_tenants.middleware.main.TenantMainMiddleware",
]

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

db_config["ENGINE"] = "django_tenants.postgresql_backend"

DATABASES = {
    "default": db_config,
}

DATABASE_ROUTERS = ("django_tenants.routers.TenantSyncRouter",)

# Compressor Settings

STATICFILES_FINDERS += ("compressor.finders.CompressorFinder",)

COMPRESS_ENABLED = False
COMPRESS_URL = "/static/"
COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
]
COMPRESS_JS_FILTERS = [
    "compressor.filters.jsmin.JSMinFilter",
]
COMPRESS_STORAGE = "compressor.storage.GzipCompressorFileStorage"
