from .base import *  # noqa
print("Homolog")

INSTALLED_APPS += ["compressor"]  # noqa F405

MIDDLEWARE += [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)

COMPRESS_ENABLED = False
COMPRESS_URL = '/static/'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'