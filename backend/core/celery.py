import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery(
    'core'
)

app.config_from_object('django.conf:settings', namespace='CELERY')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='*/1'),
        update_rates.delay(),
        name='Update exchange rates'
    )


@app.task
def update_rates():
    from exchange.models import Rates
    Rates.produce_exchange_rates()


app.autodiscover_tasks()
