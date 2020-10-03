from tacar_api.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':get_common_properties("NAME"),
        'USER':get_common_properties("PROD_USER"),
        'PASSWORD':get_common_properties("PASSWORD"),
        'HOST':get_common_properties("PROD_HOST"),
        'PORT':get_common_properties("PORT")
    }
}
