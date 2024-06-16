"""
Settings for journpy2 project.
"""

from pathlib import Path
import os
from decouple import config, Csv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",    # Use WhiteNoise in development
    "django.contrib.staticfiles",  

    # My apps
    "blog.apps.BlogConfig",
    "mainapp.apps.MainappConfig",
    'users.apps.UsersConfig',

    # Third party apps
    "django_bootstrap5",
    "cloudinary_storage",
    "cloudinary",
    "phonenumber_field",
    "django_countries",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",    # WhiteNoise middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "journpy2.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "journpy2.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Lagos"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT setting for gathering static files in a single directory so you can serve them easily.
STATIC_ROOT = BASE_DIR / "staticfiles"
# Whitenoise backend which compresses files and hashes them to unique names, so they can safely be cached forever.
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Cloudinary credentials
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('JP_CLOUD_NAME'),
    'API_KEY': config('JP_API_KEY'),
    'API_SECRET': config('JP_API_SECRET'),
}

MEDIA_URL = '/media/'  
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Custom user settings
AUTH_USER_MODEL = config('AUTH_USER_MODEL')
LOGIN_REDIRECT_URL = config('LOGIN_REDIRECT_URL')
LOGOUT_REDIRECT_URL = config('LOGOUT_REDIRECT_URL')

# Heroku settings
import django_heroku
django_heroku.settings(locals())

if os.environ.get('DEBUG') == 'TRUE':
    DEBUG = True
elif os.environ.get('DEBUG') == 'FALSE':
    DEBUG = False

