"""
Django settings for Nilam's Beauty Care website.
"""

import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# SECURITY
# -------------------------------------------------------------------
# IMPORTANT: Before deploying this website live, change SECRET_KEY to a
# new random value and set DEBUG = False.
# You can generate a new key with:
#   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-CHANGE-THIS-KEY-BEFORE-DEPLOYMENT-nilams-beauty-care'
)

# Set DEBUG = False when you deploy the site live on the internet.
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Add your live domain name here once you deploy, e.g. "nilamsbeautycare.com"
ALLOWED_HOSTS = ['*']


# -------------------------------------------------------------------
# APPLICATION DEFINITION
# -------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local app
    'salon',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nilams_beauty_care.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'salon.context_processors.salon_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'nilams_beauty_care.wsgi.application'


# -------------------------------------------------------------------
# DATABASE
# -------------------------------------------------------------------
# Simple SQLite database - works out of the box for development and
# for small/medium live sites. You can switch to PostgreSQL/MySQL later.


DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=False,
    )
}
if os.environ.get('DATABASE_URL', '').startswith('postgres'):
    DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}
# -------------------------------------------------------------------
# PASSWORD VALIDATION
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -------------------------------------------------------------------
# INTERNATIONALIZATION
# -------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# -------------------------------------------------------------------
# STATIC & MEDIA FILES
# -------------------------------------------------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------------------------------------------
# SALON BUSINESS INFO
# (used across templates via salon/context_processors.py)
# -------------------------------------------------------------------
SALON_NAME = "Nilam's Beauty Care"
SALON_ADDRESS = "Vrundavan Complex, B/9, Hirawadi Road, Bapunagar, Ahmedabad, 382345"
SALON_PHONE = "+91 98240 83685"
SALON_PHONE_RAW = "919824083685"  # used for tel: and WhatsApp links, no + or spaces
SALON_WHATSAPP = "919824083685"
# -------------------------------------------------------------------
# EMAIL NOTIFICATIONS (sent to the salon when a new booking comes in)
# -------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SALON_NOTIFY_EMAIL = os.environ.get('SALON_NOTIFY_EMAIL', EMAIL_HOST_USER)

# -------------------------------------------------------------------
# WHATSAPP NOTIFICATIONS (via the free CallMeBot service)
# -------------------------------------------------------------------
CALLMEBOT_PHONE = os.environ.get('CALLMEBOT_PHONE', '')
CALLMEBOT_APIKEY = os.environ.get('CALLMEBOT_APIKEY', '')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}