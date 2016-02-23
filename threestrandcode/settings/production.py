from .base import *


#DEBUG = False

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# Enable Connection Pooling (if desired)
DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['3strandcode.com', 'threesc-api.herokuapp.com']

# Force HTTPS links
os.environ['HTTPS'] = "on"
os.environ['wsgi.url_scheme'] = 'https'

# Social Auth
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

# Rest auth stuff
CORS_ORIGIN_WHITELIST = (
    # "localhost:8080",
    '3strandcode.com',
    'threesc-api.herokuapp.com',
)
