"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ai90q0q9s_jf^=vm!^!d^4e!zvqoho(sw#v#oylt)*m=%2*$w@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Content Security Policy

CSP_IMG_SRC = ("'self'", 'https://html.sammy-codes.com')

CSP_STYLE_SRC = ("'self'",'https://fonts.googleapis.com','https://cdn.quilljs.com/1.3.7/quill.snow.css','https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/darcula.min.css','https://cdn.jsdelivr.net/npm/quill-resize-module@1.2.4/dist/resize.min.css')

CSP_FONT_SRC = ("'self'", 'https://fonts.gstatic.com/')

CSP_SCRIPT_SRC = (
    "'self'",
    'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js',
    'https://cdn.quilljs.com/1.3.7/quill.min.js',
    'https://cdn.jsdelivr.net/npm/quill-image-compress@1.2.21/dist/quill.imageCompressor.min.js',
    'https://cdn.jsdelivr.net/npm/@botom/quill-resize-module@2.0.0/dist/quill-resize-module.min.js',
)

CSP_REPORT_ONLY = True


CSP_REPORT_ONLY_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'",  
)


CSP_REPORT_ONLY_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",  
)

#Add reporting URL for violations
CSP_REPORT_URI = '/csp-violation/'



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'csp',
    'django_quill',
    'import_export',
    'rest_framework',
    'colorfield',
]

MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'