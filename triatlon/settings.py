# coding=utf-8

"""
Django settings for triatlon project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@&dz$&hegz@0x9o77*s6x9^&(88^29nq5*q-v%n7h3_!876v5i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    u'trirotaryvaldivia.cl', u'www.trirotaryvaldivia.cl'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contacto.apps.ContactoConfig',
    #'hoteles.apps.HotelesConfig',
    #'mapachile.apps.MapachileConfig',
    'inscripcion.apps.InscripcionConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'triatlon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', '/home/trirotary/webapps/triatlon/triatlon/templates'],
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
#ftp://trirotary@207.38.94.4/home/trirotary/webapps/triatlon
WSGI_APPLICATION = 'triatlon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = ('/home/trirotary/webapps/triatlon_static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/home/trirotary/src/triatlon_static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join('media')



'''
Servers:

POP (for receiving) — mail.webfaction.com
IMAP (for receiving) — mail.webfaction.com
SMTP (for sending) — smtp.webfaction.com
Ports:

 	Standard	Secure (SSL)	Secure (TLS)
POP	110	995
IMAP	143	993
SMTP	25	465	587
Servers:

POP (for receiving) — mail.webfaction.com
IMAP (for receiving) — mail.webfaction.com
SMTP (for sending) — smtp.webfaction.com
Ports:

 	Standard	Secure (SSL)	Secure (TLS)
POP 	110     	995
IMAP	143     	993
SMTP	25	        465	            587
'''
ADMINS = (('Contacto', 'contacto@trirotaryvaldivia.cl'))
WEBFACTION = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

if WEBFACTION is True:
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.webfaction.com'
    EMAIL_HOST_USER = 'noresponder_rotary'
    EMAIL_HOST_PASSWORD = '123triatlon'
    # EMAIL_SSL_KEYFILE = None
    DEFAULT_FROM_EMAIL = 'noresponder@trirotaryvaldivia.cl'
    # SERVER_EMAIL = 'noresponder@trirotaryvaldivia.cl'
    # DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

else:
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'hernanfontanez@gmail.com'
    EMAIL_HOST_PASSWORD = 'xxxx'

