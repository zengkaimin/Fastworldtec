from pathlib import Path  # Import Path class for path operations

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent  # Define the base directory of the project

# SECURITY WARNING: keep the secret key used in production secret! Secret key for cryptographic operations
SECRET_KEY = 'django-insecure-$5!nvt8*m_72m2i#bvwlusi*bqm47%(fe+q^96p_#+k2ev6but'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Debug mode toggle (set to False in production)

ALLOWED_HOSTS = ['*']  # List of allowed hosts for the application

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # Django admin app
    'django.contrib.auth',  # Django authentication app
    'django.contrib.contenttypes',  # Django content types app
    'django.contrib.sessions',  # Django sessions app
    'django.contrib.messages',  # Django messages app
    'django.contrib.staticfiles',  # Django static files app

    # local apps
    'homepage.apps.HomepageConfig',  # Local app: Homepage
    'software.apps.SoftwareConfig',  # Local app: Software
    'FeedingSupplies.apps.FeedingSuppliesConfig',  # Local app: Feeding Supplies
    'SleepEssentials.apps.SleepEssentialsConfig',  # Local app: Sleep Essentials   
    'BabyClothes.apps.BabyclothesConfig',  # 添加这一行
    'toiletries.apps.ToiletriesConfig',
    'DailyEssentials.apps.DailyEssentialsConfig',  # Local app: Daily Essentials
    'LargeItems.apps.LargeItemsConfig',  # Local app: Large Items
    'mdeditor',  # Added mdeditor
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',  # 会话中间件放在最前
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
     #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Beginmama.urls'  # Root URL configuration module

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Template backend
        'DIRS': [BASE_DIR / 'templates', ],  # Directories to search for templates
        'APP_DIRS': True,  # Whether to look for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Debug context processor
                'django.template.context_processors.request',  # Request context processor
                'django.contrib.auth.context_processors.auth',  # Authentication context processor
                'django.contrib.messages.context_processors.messages',  # Messages context processor
            ],
        },
    },
]

WSGI_APPLICATION = 'Beginmama.wsgi.application'  # WSGI application module

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'data' / 'db.sqlite3',
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        # Validator for attribute similarity
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Validator for minimum length
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Validator for common passwords
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Validator for numeric passwords
    },
]

# Internationalization

LANGUAGE_CODE = 'en-us'  # Default language code

TIME_ZONE = 'Asia/Shanghai'  # Default time zone

USE_I18N = True  # Enable internationalization

USE_TZ = True  # Enable timezone-aware datetime

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'  # URL prefix for static files
STATIC_ROOT = BASE_DIR / 'static'  # Directory to collect static files

STATICFILES_DIRS = ['static/local_static/', ]  # Additional directories to look for static files

MEDIA_URL = 'media/'  # URL prefix for media files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory to store media files

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default field type for auto-created primary keys

# Session 配置
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # 使用数据库存储会话
SESSION_COOKIE_AGE = 1209600  # 会话过期时间，2周
SESSION_COOKIE_NAME = 'fastworldtec_sessionid'  # 自定义会话cookie名称
SESSION_COOKIE_SECURE = True  # 开发环境使用 HTTP
SESSION_COOKIE_HTTPONLY = True  # 防止 JavaScript 访问会话 cookie
SESSION_SAVE_EVERY_REQUEST = False  # 不是每个请求都保存会话

# 缓存配置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-fastworldtec',
        'TIMEOUT': 300,  # 5分钟缓存过期
        'OPTIONS': {
            'MAX_ENTRIES': 1000,  # 最大缓存条目
            'CULL_FREQUENCY': 3,  # 清理频率
        }
    }
}

# 安全相关配置
CSRF_COOKIE_SECURE = False  # 开发环境使用 HTTP
CSRF_COOKIE_HTTPONLY = True
CSRF_USE_SESSIONS = True  # 将 CSRF 令牌存储在会话中而不是 cookie 中
