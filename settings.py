DATABASES = {
    'postgresql_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quickdb',
        'USER': 'sonarsource',
        'PASSWORD': 'test123', # Noncompliant
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
