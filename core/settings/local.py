from .base import *  # noqa

print("Local")

THIRD_PARTY_APPS += ["django_extensions"]  # noqa F405

SHARED_APPS = DJANGO_APPS + THIRD_PARTY_APPS

INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

ROOT_URLCONF = "core.urls"

DATABASES = {
    "default": db_config,
}
