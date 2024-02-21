INSTALLED_APPS = [    ...    'tasks', 'rest_framework', 'corsheaders']

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'wengb159753@gmail.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Selectagb.1597532604'