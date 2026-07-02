from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ── SEGURIDAD ──────────────────────────────────────────────────────────────
SECRET_KEY = 'django-insecure-cambia-esta-clave-en-produccion-!!!!'
DEBUG = False
ALLOWED_HOSTS = [
    "guerreros-cf.onrender.com",
    "localhost",
    "127.0.0.1",
]

# ── APLICACIONES ──────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # App principal
    'guerreros_cf',
]

# ── MIDDLEWARE ─────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF  = 'guerreros_proyecto.urls'
WSGI_APPLICATION = 'guerreros_proyecto.wsgi.application'

# ── TEMPLATES ─────────────────────────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],      # templates globales
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

# ── BASE DE DATOS ──────────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':   BASE_DIR / 'db.sqlite3',
        # Para MySQL/PostgreSQL en producción:
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME':   'guerreros_db',
        # 'USER':   'guerreros_user',
        # 'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        # 'HOST':   'localhost',
        # 'PORT':   '5432',
    }
}

# ── CONTRASEÑAS ────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── INTERNACIONALIZACIÓN ───────────────────────────────────────────────────
LANGUAGE_CODE = 'es-mx'
TIME_ZONE     = 'America/Mexico_City'
USE_I18N      = True
USE_TZ        = True

# ── ARCHIVOS ESTÁTICOS ─────────────────────────────────────────────────────
STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / "static_guerreros_cf",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# ── ARCHIVOS DE MEDIA (subidos por usuarios) ───────────────────────────────
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ── DEFAULT PK ────────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── EMAIL (para notificaciones de contacto e inscripciones) ───────────────
EMAIL_BACKEND       = 'django.core.mail.backends.console.EmailBackend'  # dev
# En producción usar SMTP:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'santitosmm92@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_contraseña_de_aplicacion'
DEFAULT_FROM_EMAIL  = 'guerrerscf@gmail.com'
ADMIN_EMAIL         = 'guerrerscf@gmail.com'
