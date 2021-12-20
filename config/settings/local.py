from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dev_toss',
        'USER': get_secret('LOCAL_DB_USER'),
        'PASSWORD': get_secret('LOCAL_DB_PASSWORD'),
        'HOST': get_secret('LOCAL_DB_HOST'),
        'PORT': get_secret('LOCAL_DB_PORT'),
    }
}