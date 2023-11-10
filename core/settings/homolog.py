from .base import *  # noqa

print("Homolog")

# Application definition

THIRD_PARTY_APPS += ["compressor"]  # noqa F405

SHARED_APPS = DJANGO_APPS + THIRD_PARTY_APPS

INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

# Compressor Cache Middleware

CACHE_MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]

MIDDLEWARE = MIDDLEWARE + CACHE_MIDDLEWARE

ROOT_URLCONF = "core.urls"

# Database Settings

DATABASES = {
    "default": db_config,
}

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
