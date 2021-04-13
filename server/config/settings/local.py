from .base import *  # noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="839e71f2ae2d41dd2e94dcac525cf7b58566f9f04f6cb25a959369dc97f39a71",
)

DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
