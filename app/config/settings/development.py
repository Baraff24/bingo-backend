from .base import *

# Media and static files
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../../vol/', 'mediafiles')

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../../vol/', 'staticfiles')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
