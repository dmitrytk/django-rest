from .base import *  # noqa
from .base import env

DEBUG = True
SECRET_KEY = env("DJANGO_SECRET_KEY")
