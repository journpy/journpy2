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
    # Default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",    # Use WhiteNoise in development
    "django.contrib.staticfiles",

    # Third party apps
    "django_bootstrap5",
    "phonenumber_field",
    "django_countries",
    "markdownfield",        # render Markdown and store it in the database.
    "pwa",

    # Local apps
    "learn.apps.LearnConfig",
    "blog.apps.BlogConfig",
    "mainapp.apps.MainappConfig",
    "users.apps.UsersConfig",
    "contact.apps.ContactConfig",
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
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
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
        "OPTIONS": {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
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

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Custom user settings
AUTH_USER_MODEL = config('AUTH_USER_MODEL')
LOGIN_REDIRECT_URL = config('LOGIN_REDIRECT_URL')
LOGOUT_REDIRECT_URL = config('LOGOUT_REDIRECT_URL')

# SMTP server configuration and your credentials
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
SERVER_EMAIL = config('SERVER_EMAIL')
ADMINS = [('JournPy', 'journpy@gmail.com')]

if os.environ.get('DEBUG') == 'TRUE':
    DEBUG = True
elif os.environ.get('DEBUG') == 'FALSE':
    DEBUG = False

# for django-markdownfield
SITE_URL = config("SITE_URL")

# configuring pwa manifest members
PWA_APP_NAME = 'JournPy'
PWA_APP_DESCRIPTION = "An app that offers concise tutorials on programming languages and frameworks."
PWA_APP_THEME_COLOR = '#4062AD'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/images/jpy_pwa_icon.png',
        'sizes': '2481x2481'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/images/jpy_pwa_icon.png',
        'sizes': '2481x2481'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/journpy12@300x.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
PWA_APP_SHORTCUTS = [
    {
        'name': 'Login',
        'url': 'https://journpy.pythonanywhere.com/users/login/',
        'description': 'Shortcut to Login page',
        "icons": [
            {
                'src': '/static/images/login_shortcut.png',
                'sizes': '96x96'
            }
                ]
    },
    {
        'name': 'Blog',
        'url': 'https://journpy.pythonanywhere.com/blogs/',
        'description': 'Shortcut to Blogs',
        'icons': [
            {
                'src': '/static/images/blog_shortcut.png',
                'sizes': '96x96'
            }
                ]
    },

    {
        'name': 'Learn Python',
        'url': 'https://journpy.pythonanywhere.com/python_tutorial/',
        'description': 'Learn Python Shortcut',
        'icons': [
            {
                'src': '/static/images/jpylearn_py.png',
                'sizes': '96x96'
            }
                ]
        },
]
PWA_APP_SCREENSHOTS = [
    {
      'src': '/static/images/jpy_pwa_icon.png',
      'sizes': '2481x2481',
      "type": "image/png"
    }
]

