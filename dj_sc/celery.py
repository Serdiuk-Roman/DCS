from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import json


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_sc.settings')

app = Celery('dj_sc')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task(bind=True)
def item_to_db(self, item):
    from main_page.models import PorterItem
    item = json.loads(item)
    PorterItem.objects.get_or_create(
        designer_name=item['designer_name'],
        link=item['link'],
        product_name=item['product_name'],
        price=item['price'],
        currency=item['currency'],
        size=item['size'],
        description=item['description'],
        images=item['images'],
    )
