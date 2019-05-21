from .common import *

PUBLIC_REGISTER_ENABLED = False
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = '$TAIGA_SECRET'

MEDIA_URL = "$TAIGA_SCHEME://$TAIGA_HOST/media/"
STATIC_URL = "$TAIGA_SCHEME://$TAIGA_HOST/static/"
ADMIN_MEDIA_PREFIX = "$TAIGA_SCHEME://$TAIGA_HOST/static/admin/"
SITES["api"]["scheme"] = "$TAIGA_SCHEME"
SITES["api"]["domain"] = "$TAIGA_HOST"
SITES["front"]["scheme"] = "$TAIGA_SCHEME"
SITES["front"]["domain"] = "$TAIGA_HOST"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "$POSTGRES_DB",
        "HOST": "$POSTGRES_HOST",
        "USER": "$POSTGRES_USER",
        "PASSWORD": "$POSTGRES_PASSWORD"
    }
}

#DEFAULT_FROM_EMAIL = "john@doe.com"
#CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 #seconds
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = False
#EMAIL_USE_SSL = False # You cannot use both (TLS and SSL) at the same time!
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'user'
#EMAIL_HOST_PASSWORD = 'password'

set_email_backend = $SET_EMAIL_BACKEND
set_email_use_ssl = $SET_EMAIL_USE_SSL

if set_email_backend:
    CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    if set_email_use_ssl:
        EMAIL_USE_SSL = True
    else:
        EMAIL_USE_TLS = True
    EMAIL_HOST = '$SET_EMAIL_HOST'
    EMAIL_PORT = $SET_EMAIL_PORT
    EMAIL_HOST_USER = '$SERVER_EMAIL_USER'
    EMAIL_HOST_PASSWORD = '$SERVER_EMAIL_PASSWORD'

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://$RABBIT_USER:$RABBIT_PASSWORD@$RABBIT_HOST:$RABBIT_PORT/$RABBIT_VHOST"}
