import os

from .base import *  # noqa
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = ('rest_framework.renderers.JSONRenderer',)
