# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.utils.serialize import ScrapyJSONEncoder
from dj_sc.celery import item_to_db

encoder = ScrapyJSONEncoder()


class TutorialPipeline(object):
    def process_item(self, item, spider):
        # celery task(item)
        item_to_db.delay(encoder.encode(item))
        return item
