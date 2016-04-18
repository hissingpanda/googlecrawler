# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings

class MongoDBPipeline(object):
	# make connection to crawlerdb
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERV'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
    	# insert item into items collection
        self.collection.insert(dict(item))
        return item