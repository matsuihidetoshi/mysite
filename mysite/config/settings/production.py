from .base import *

STATICFILES_DIRS = (
    os.path.join(ANOTHER_BASE_DIR, 'static'),  # プロジェクト直下のstaticディレクトリを指定
)

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


DEBUG = False

ALLOWED_HOSTS = [".mattle.work", "18.216.125.136"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'production': {
            'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
                      '%(pathname)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/django.log',
            'formatter': 'production',
            'when': 'D', # 単位は日
            'interval': 1, # 一日おき
            'backupCount': 7, # 世代数
        },
    },
    'loggers': {
        # 自作したログ出力
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Djangoの警告・エラー
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
