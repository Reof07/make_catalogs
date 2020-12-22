from .base import *
from .base import env

DEBUG=False

ALLOWED_HOSTS = ['*']

MIDDLEWARE = ('whitenoise.middleware.WhiteNoiseMiddleware',)


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

 
 # Update database configuration with $DATABASE_URL.
import dj_database_url  
db_from_env = dj_database_url.config(conn_max_age=500)  
DATABASES['default'].update(db_from_env)

