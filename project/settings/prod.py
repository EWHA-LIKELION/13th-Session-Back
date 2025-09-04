from .base import *

environ.Env.read_env(os.path.join(BASE_DIR, '.env.prod'))

DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
