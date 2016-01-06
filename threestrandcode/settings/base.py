"""
Django settings for threestrandcode project on Heroku. Fore more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import sys
import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Also add ./apps to python path
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "0-hc)b&z+8f1r0uz*7_^4!4&5pu80qi!gcqbhu1t%g)(313(5*"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition
THIRD_PARTY_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_auth',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'django_extensions',
    'social.apps.django_app.default',
    'corsheaders',
)
OUR_APPS = (
    'pages',
    'applicants',
    'api',
    'homework',
)
INSTALLED_APPS = THIRD_PARTY_APPS + OUR_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'threestrandcode.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'threestrandcode.wsgi.application'

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Django rest framework.
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # Let's make everything require admin permissions by default
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'api.serializers.EmailLoginSerializer',
}

# Python Social Auth
AUTHENTICATION_BACKENDS = (
    'utils.authentication_backends.UserModelEmailBackend',
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.github.GithubOAuth2',
)
SOCIAL_AUTH_GITHUB_KEY = os.environ.get("GITHUB_KEY")
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get("GITHUB_SECRET")

if not os.environ.get("CIRCLECI"):
    assert SOCIAL_AUTH_GITHUB_KEY and SOCIAL_AUTH_GITHUB_SECRET, "Missing Github API key env vars"

# We don't want to add a new user, just modify some user detail
SOCIAL_AUTH_PIPELINE = (
    'applicants.social_pipeline.ensure_logged_in',
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'applicants.social_pipeline.save_github_name',
    'social.pipeline.user.user_details',
)

CORS_ORIGIN_ALLOW_ALL = True
