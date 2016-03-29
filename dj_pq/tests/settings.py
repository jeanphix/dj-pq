import dj_database_url


db_config = dj_database_url.config()

DATABASES = dict(
    default=db_config,
    another=db_config,
)

SECRET_KEY = 'secret'

INSTALLED_APPS = ['dj_pq']
