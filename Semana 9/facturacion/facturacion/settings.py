"""
Django settings for facturacion project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4tdh7n(i75+b9noel^=_b8=h8@idsvq#_o(g2_k^ed=yv7u=mv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['facturacion-django-eduardo.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'restaurante',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'facturacion.urls'

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

WSGI_APPLICATION = 'facturacion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eqr5vit31wuhxe8r',  # DATABASE
        'USER': 'jv42m34azibjx9ed',  # USERNAME
        'PASSWORD': 'x68vued9or6snaco',
        'HOST': 'pxukqohrckdfo4ty.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Al nosotros sobreescribir el modelo de usuario tenemos que indicar a Django
AUTH_USER_MODEL = 'restaurante.PersonalModel'

# sirve para indicar donde se guardaran todos los archivos pasados por el client (FileField o ImageField)
MEDIA_URL = '/media/'
# sirve para mostrar el archivo multimedia mediante una URL
MEDIA_ROOT = BASE_DIR / 'media'

# HABILITAMOS LOS CORS
CORS_ALLOW_ALL_ORIGINS = True

# Para modificar configurarciones de Django-rest-framework se hace mediante la variable REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
# Para modificar la configuracion predeterminada de nuestro simple-jwt
# para ver todas las opciones de configuracion => https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html#
SIMPLE_JWT = {
    # sirve para indicar la pk de nuestra tabla user si es que la hemos cambiado (x defecto es 'id')
    'USER_ID_FIELD': 'personalId',
    # sirve para indicar cuanto de vida va a tener la token de ACCESSO
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    # sirve para indicar que algoritmo va a usar para encriptar la token
    'ALGORITHM': 'HS256',  # 'HS384', 'HS512',
    # sirve para indicar mediante que palabra va a utilizar para identificar la token
    'AUTH_HEADER_TYPES': ('Bearer', ),
    # si el usuario acepta renovar la sesion la token de acceso que se creará sera con un tiempo de vida de un dia
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)

}

# para que cuando hagamos py manage.py collectstatic genere todos los assets en la carpeta que le indicamos a continuacion
STATIC_ROOT = BASE_DIR / 'assets/'
