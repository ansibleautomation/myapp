from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myapp_db',
        'USER': 'www',
        'HOST': '127.0.0.1',
    },
}
