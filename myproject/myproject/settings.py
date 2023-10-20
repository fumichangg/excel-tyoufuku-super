from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", 'django-insecure-)u^r9^lo3x0_)2-74txqnxrn15w!o!le2=6)*tk*498_thda35')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = ['*']  # You should be more specific in production!

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'excelapp',
    'whitenoise.runserver_nostatic',  # <--- Add this for Whitenoise
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <--- Add this for Whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    # ... (no changes here)
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3'))
}

# Password validation
# ... (no changes here)

# Internationalization
# ... (no changes here)

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # <-- Add this for Whitenoise
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# At the very bottom of the file, add these lines to apply Django-Heroku optimizations
import django_heroku
django_heroku.settings(locals())
