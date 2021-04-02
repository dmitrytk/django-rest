from .base import *  # noqa
from .base import env

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])

# sentry_sdk.init(
#     dsn="https://627974e1f0c144b583cc909e641554e3@o527514.ingest.sentry.io/5643856",
#     integrations=[DjangoIntegration()],
#     traces_sample_rate=1.0,
#     send_default_pii=True,
# )
