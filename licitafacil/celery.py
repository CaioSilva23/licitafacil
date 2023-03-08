import os
from celery import Celery
from django.conf import settings
# celery -A projeto_celery worker --loglevel=INFO

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'licitafacil.settings')

app = Celery('licitafacil')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')