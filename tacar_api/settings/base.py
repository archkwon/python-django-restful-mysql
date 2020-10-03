import json
import os
import sys
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

with open(os.path.join(BASE_DIR, 'properties.json')) as f:
    secrets = json.loads(f.read())


def get_common_properties(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_common_properties("SECRET_KEY")

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# Application definition
INSTALLED_APPS = [
    'rest_framework',
    'api_login',
    'api_user',
    'api_cust',
    'api_order',
    'api_location',
    'corsheaders',
    'rangefilter',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'tacar_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'tacar_api.wsgi.application'

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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


STATIC_URL = '/static/'
STATIC_DIR =  os.path.join(BASE_DIR, 'static')

MEDIA_URL =  '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(BASE_DIR, '.static_root')


#CUSTOM VARIABLE
REQUESTS_HEADER = {"Content-Type": "application/json; charset=UTF-8"}

FCM_KEY = get_common_properties("FCM_KEY")

NAVER_SMS_API_URL = get_common_properties("NAVER_SMS_API_URL")

NAVER_SMS_API_URI = get_common_properties("NAVER_SMS_API_URI")

NAVER_SERVICE_ID = get_common_properties("NAVER_SERVICE_ID")

NAVER_ACCESS_KEY = get_common_properties("NAVER_ACCESS_KEY")

NAVER_SECRET_KEY = get_common_properties("NAVER_SECRET_KEY")

NAVER_CALL_NUMBER = get_common_properties("NAVER_CALL_NUMBER")

NAVER_SMS_TIME_LIMIT = get_common_properties("NAVER_SMS_TIME_LIMIT")

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'tacar_api.settings.prod':
    MUZIN_ERP_API_URL = "http://" + get_common_properties("PROD_HOST") + ":9091"
    KIN_DRIVER_API_URL = "http://" + get_common_properties("PROD_HOST_DRIVER_AWS")

elif os.environ.get('DJANGO_SETTINGS_MODULE') == 'tacar_api.settings.dev':
    MUZIN_ERP_API_URL = "http://" + get_common_properties("DEV_HOST") + ":9091"
    KIN_DRIVER_API_URL = "http://" + get_common_properties("DEV_HOST")

elif os.environ.get('DJANGO_SETTINGS_MODULE') == 'tacar_api.settings.local':
    MUZIN_ERP_API_URL = "http://" + get_common_properties("LOCAL_HOST") + ":9091"
    KIN_DRIVER_API_URL = "http://" + get_common_properties("LOCAL_HOST") + ":9000"

else:
    raise ValueError('Invalid environment name')
